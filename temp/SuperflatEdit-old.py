import numpy as np
from datetime import datetime
from multiprocessing import Manager
from mca import Region, Block, EmptyRegion, EmptyChunk
import os, ast, copy, time, argparse, tempfile, threading, multiprocessing

manager = Manager()
names = manager.dict()

def SuperflatEdit(Layer_of_blocks, blocklist, save_path, mca_file):
    chunkList = {}
    new_chunk_set = {}
    new_region_set = {}
    empty_chunk = manager.dict()

    print(datetime.now().strftime("%H:%M:%S"), 'A')

    # for ax in range(32):
    #     for az in range(32):
    #         names['empty_chunk_emptychunk_%s_%s' % (ax, az)] = Region.from_file(mca_file).get_chunk(ax, az)
    # 改为如下多进程

    def process_empty_chunk(ax, az, mca_file, empty_chunk):
        empty_chunk['%s_%s' % (ax, az)] = Region.from_file(mca_file).get_chunk(ax, az)

    processes = []
    
    for ax in range(32):
        for az in range(32):
            process = Process(target=process_empty_chunk, args=(ax, az, mca_file, empty_chunk))
            processes.append(process)
            process.start()

    for process in processes:
        process.join()

    print(datetime.now().strftime("%H:%M:%S"), 'B')

    # for block in blocklist:
    #     id, x, y, z = block
    #     if 'new_region_%s_%s' % (x // 512, z // 512) not in new_region_set.keys():
    #         names['new_region_%s_%s' % (x // 512, z // 512)] = EmptyRegion(0, 0)
    #         new_region_set['new_region_%s_%s' % (x // 512, z // 512)] = [names['new_region_%s_%s' % (x // 512, z // 512)], x // 512, z // 512]
    #         names['new_region_%s_%s' % (x // 512, z // 512)].add_chunk(empty_chunk[item]) for item in list(empty_chunk.keys())
    #     if 'new_chunk_%s_%s' % (x // 16, z // 16) not in new_chunk_set.keys():
    #         names['new_chunk_%s_%s' % (x // 16, z // 16)] = EmptyChunk((x % 512) // 16, (z % 512) // 16)
    #         new_chunk_set['new_chunk_%s_%s' % (x // 16, z // 16)] = [names['new_chunk_%s_%s' % (x // 16, z // 16)], x // 512, z // 512]
    #     chunkList['Chunk(%s,%s)' % (x // 16, z // 16)] = range(-64, 320)
    # 用numpy矩阵重写

    data_array = np.array(blocklist)
    result_pairs = set(zip(data_array[:, 1].astype(int) // 512, data_array[:, 3].astype(int) // 512, data_array[:, 1].astype(int) // 16, data_array[:, 3].astype(int) // 16, (data_array[:, 1].astype(int) % 512) // 16, (data_array[:, 3].astype(int) % 512) // 16))

    for block in list(result_pairs):
        a, b, c, d, e, f = block
        if 'new_region_%s_%s' % (a, b) not in new_region_set.keys():
            names['new_region_%s_%s' % (a, b)] = EmptyRegion(0, 0)
            new_region_set['new_region_%s_%s' % (a, b)] = [names['new_region_%s_%s' % (a, b)], a, b]
            [names['new_region_%s_%s' % (a, b)].add_chunk(empty_chunk[item]) for item in list(empty_chunk.keys())]
        if 'new_chunk_%s_%s' % (c, d) not in new_chunk_set.keys():
            names['new_chunk_%s_%s' % (c, d)] = EmptyChunk(e, f)
            new_chunk_set['new_chunk_%s_%s' % (c, d)] = [names['new_chunk_%s_%s' % (c, d)], a, b]
        chunkList['Chunk(%s,%s)' % (c, d)] = range(-64, 320)

    ChunkDict = {i: {} for i in list(chunkList.keys())}

    print(datetime.now().strftime("%H:%M:%S"), 'C')

    for i in range(list(chunkList.keys())):
        for block_index in range(-64, 320):
            ChunkDict[list(chunkList.keys())[i]][block_index] = [[[Layer_of_blocks[str(block_index)] for _ in range(16)] for _ in range(16)] if (str(block_index) in Layer_of_blocks.keys()) else [['air' for _ in range(16)] for _ in range(16)]][0]

    # ChunkDict = copy.deepcopy(ChunkDict) # 试试没有深拷贝行不行，确实昂贵操作这

    print(datetime.now().strftime("%H:%M:%S"), 'D')

    for block in blocklist:
        id, x, y, z = block
        ChunkDict['Chunk({},{})'.format(x//16, z//16)][y][z % 16][x % 16] = id

    print(datetime.now().strftime("%H:%M:%S"), 'E')

    for l in list(ChunkDict):
        for m in ChunkDict[l].keys():
            for z, n in enumerate(ChunkDict[l][m]):
                for x, id in enumerate(ChunkDict[l][m][z]):
                    names['new_chunk_%s_%s' % (l[6:-1].split(",")[0], l[6:-1].split(",")[1])].set_block(Block(id), x, int(m), z)

    # for chunk in list(new_chunk_set):
    #     names['new_region_%s_%s' % (new_chunk_set[chunk][1], new_chunk_set[chunk][2])].add_chunk(new_chunk_set[chunk][0])
    # 
    # 改为如下多进程

    def process_chunk(region_x, region_z, new_chunk_set, names):
        names['new_region_%s_%s' % (region_x, region_z)].add_chunk(new_chunk_set[chunk])

    processes = []
    
    for chunk in list(new_chunk_set):
        process = Process(target=process_chunk, args=(new_chunk_set[chunk][1], new_chunk_set[chunk][2], new_chunk_set[chunk][0], names))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print(datetime.now().strftime("%H:%M:%S"), 'F')

    # for region in list(new_region_set):
    #     new_region_set[region][0].save(os.path.join(save_path, 'r.{}.{}.mca'.format(new_region_set[region][1], new_region_set[region][2])))
    # 
    # 改为如下多线程
    
    def save_region(region_info):
        region, x, z = region_info
        region.save(os.path.join(save_path, 'r.{}.{}.mca'.format(x, z)))

    threads = []

    for region in list(new_region_set):
        region_info = (new_region_set[region][0], new_region_set[region][1], new_region_set[region][2])
        thread = threading.Thread(target=save_region, args=(region_info,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(datetime.now().strftime("%H:%M:%S"), 'G')


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-w', required=True, help='Path to the world folder')
    parser.add_argument('-b', required=True, help='Path to the blocklist file')
    parser.add_argument('-m', help='Path to the r.0.0.mca file')
    parser.add_argument('-s', help='Layers of the blocks')

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
        content = file.read()
    blocklist = ast.literal_eval(content)

    Layer_of_blocks = {}
    for pair in s.split(';'):
        key, value = pair.split(':')
        Layer_of_blocks[key] = value

    SuperflatEdit(save_path=save_path, Layer_of_blocks=Layer_of_blocks, blocklist=blocklist, mca_file=mca_file)
