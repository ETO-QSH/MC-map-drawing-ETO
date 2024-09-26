from itertools import chain
from mcworldlib.anvil import load_region
import os, ast, copy, math, numpy, argparse, tempfile
from nbtlib.tag import Int, Byte, List, Long, Short, String, Compound, LongArray

def SuperflatEdit(Layer_of_blocks, blocklist, save_path, mca_file):

    result_dict, int_64_max, data_array, Data_model, I2B = {}, 2**63, numpy.array(blocklist), load_region(mca_file), lambda num, bits: bin(num)[2:].zfill(bits)
    result_pairs = set(zip(data_array[:, 1].astype(int)//512, data_array[:, 3].astype(int)//512, (data_array[:, 1].astype(int)%512)//16, (data_array[:, 3].astype(int)%512)//16))
    sections = {k: v for d in [{str(Y): [list(chain(*[[Layer_of_blocks[str(Y*16+i)] for _ in range(256)] if str(Y*16+i) in Layer_of_blocks.keys() else ['air' for _ in range(256)] for i in range(16)]))
                if Y in numpy.array(list(Layer_of_blocks.keys())).astype(int)//16 else ['air' for _ in range(4096)]][0]} for Y in range(-4, 20)] for k, v in d.items()}

    for item in result_pairs:
        a, b, c, d = item
        if f"{a}_{b}" in result_dict:
            result_dict[f"{a}_{b}"][f"{c}_{d}"] = copy.deepcopy(sections)
        else:
            result_dict[f"{a}_{b}"] = {f"{c}_{d}": copy.deepcopy(sections)}

    for block in blocklist:
        id, x, y, z = block
        region, chunk, section = f"{x//512}_{z//512}", f"{(x%512)//16}_{(z%512)//16}", str(y//16)
        if region in result_dict and chunk in result_dict[region] and section in result_dict[region][chunk]:
            result_dict[region][chunk][section][(y%16)*256+((z%512)%16)*16+(x%512)%16] = id

    for region in result_dict.keys():
        updata_Flag, Data = False, copy.deepcopy(Data_model)
        for Chunk in Data.keys():
            mca_chunk = str(Chunk).replace(" ", "").replace(",", "_")[1:-1]
            Data[Chunk]['isLightOn'], Data[Chunk]['LastUpdate'], Data[Chunk]['InhabitedTime'] = Byte(0), Long(0), Long(0)
            if mca_chunk in result_dict[region]:
                for entries in result_dict[region][mca_chunk].keys():
                    blocks = sorted(list(set(result_dict[region][mca_chunk][entries])), key=lambda name: {'air': 0, 'glass': 1}.get(name, 2))
                    updataBlocks = [Short(int(((i%256)//16)*256 + (i//256)*16 + i%16)) for i, block in enumerate(result_dict[region][mca_chunk][entries]) if block != 'air']
                    updata_Flag, datas, bite = True, [], (lambda n: 4 if n < 16 else math.ceil(math.log2(n+1)))(len(blocks) - 1)
                    section = [I2B(blocks.index(i), bite) for i in result_dict[region][mca_chunk][entries]]
                    new_palette = List([Compound({'Name': String(':'.join(['minecraft', item]))}) for item in blocks])
                    Data[Chunk]['xPos'], Data[Chunk]['zPos'] = Int(int(mca_chunk.split("_")[0])), Int(int(mca_chunk.split("_")[1]))
                    for i in range(math.ceil(4096/(64//bite))):
                        int_64 = int(''.join(map(str, section[i*(64//bite): (i+1)*(64//bite)][::-1])).zfill(64), 2)
                        datas.append(Long(int_64)) if int_64_max > int_64 else datas.append(Long(int_64-2*int_64_max))
                    for i in range(len(Data[Chunk]['sections'])):
                        if int(Data[Chunk]['sections'][i]['Y']) == int(entries):
                            Data[Chunk]['sections'][i]['block_states']['data'] = LongArray(datas)
                            Data[Chunk]['sections'][i]['block_states']['palette'] = new_palette
                            Data[Chunk]['PostProcessing'][i] = List(updataBlocks)
        Data.save(os.path.join(save_path, 'r.{}.{}.mca'.format(*region.split('_')))) if updata_Flag == True else None

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-w', required=True, help='Path to the world folder')
    parser.add_argument('-b', required=True, help='Path to the blocklist file')
    parser.add_argument('-s', required=True, help='Layers of the blocks')
    parser.add_argument('-m', help='Path to the r.0.0.mca file')

    args = parser.parse_args()

    def find_path(directory):
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith("mca") and file.startswith("r.0.0"):
                    return os.path.join(root, file)
        return None

    mca_file = find_path(tempfile.gettempdir())
    mca_file = mca_file if mca_file != None else args.m

    save_path = args.w
    s = args.s if args.s != None else '-64:bedrock;-63:dirt;-62:dirt;-61:grass_block'

    with open(args.b, 'r') as file:
        blocklist = ast.literal_eval(file.read())

    Layer_of_blocks = {}
    for pair in s.split(';'):
        key, value = pair.split(':')
        Layer_of_blocks[key] = value

    SuperflatEdit(save_path=save_path, Layer_of_blocks=Layer_of_blocks, blocklist=blocklist, mca_file=mca_file)
