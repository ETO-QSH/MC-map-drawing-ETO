from mca import Region, Block, EmptyRegion, EmptyChunk
import os, ast, copy, argparse, tempfile

names = locals()

def SuperflatEdit(Layer_of_blocks, blocklist, world_folder, mca_file):
    chunkList = {}
    new_chunk_set = {}
    new_region_set = {}

    for ax in range(32):
        for az in range(32):
            names['empty_chunk_emptychunk_%s_%s' % (ax, az)] = Region.from_file(mca_file).get_chunk(ax, az)

    for block in blocklist:
        id, x, y, z = block
        if 'new_region_%s_%s' % (x // 512, z // 512) not in new_region_set.keys():
            names['new_region_%s_%s' % (x // 512, z // 512)] = EmptyRegion(0, 0)
            new_region_set['new_region_%s_%s' % (x // 512, z // 512)] = [names['new_region_%s_%s' % (x // 512, z // 512)], x // 512, z // 512]
            for ax in range(32):
                for az in range(32):
                    names['new_region_%s_%s' % (x // 512, z // 512)].add_chunk(names['empty_chunk_emptychunk_%s_%s' % ((x % 512) // 16, (z % 512) // 16)])
        if 'new_chunk_%s_%s' % (x // 16, z // 16) not in new_chunk_set.keys():
            names['new_chunk_%s_%s' % (x // 16, z // 16)] = EmptyChunk((x % 512) // 16, (z % 512) // 16)
            new_chunk_set['new_chunk_%s_%s' % (x // 16, z // 16)] = [names['new_chunk_%s_%s' % (x // 16, z // 16)], x // 512, z // 512]
        chunkList['Chunk(%s,%s)' % (x // 16, z // 16)] = range(-64, 320)

    ChunkDict = {i: {} for i in list(chunkList.keys())}

    for i, _ in enumerate(list(chunkList.keys())):
        for block_index in range(-64, 320):
            try:
                block_grid = [[Layer_of_blocks[str(block_index)] for _ in range(16)] for _ in range(16)]
            except KeyError:
                block_grid = [['air' for _ in range(16)] for _ in range(16)]

            ChunkDict[list(chunkList.keys())[i]][block_index] = block_grid

    ChunkDict = copy.deepcopy(ChunkDict)

    for block in blocklist:
        id, x, y, z = block
        ChunkDict['Chunk({},{})'.format(x//16, z//16)][y][z%16][x%16] = id

    for l in list(ChunkDict):
        for m in ChunkDict[l].keys():
            for z, n in enumerate(ChunkDict[l][m]):
                for x, id in enumerate(ChunkDict[l][m][z]):
                    names['new_chunk_%s_%s' % (l[6:-1].split(",")[0], l[6:-1].split(",")[1])].set_block(Block(id), x, int(m), z)

    for chunk in list(new_chunk_set):
        names['new_region_%s_%s' % (new_chunk_set[chunk][1], new_chunk_set[chunk][2])].add_chunk(new_chunk_set[chunk][0])

    for region in list(new_region_set):
        new_region_set[region][0].save(world_folder+'\\region\\'+'r.{}.{}.mca'.format(new_region_set[region][1], new_region_set[region][2]))


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-w', required=True, help='Path to the world folder')
    parser.add_argument('-b', required=True, help='Path to the blocklist file')
    parser.add_argument('-s', help='Layers of the blocks')

    args = parser.parse_args()

    def find_path(directory):
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith("mca") and file.startswith("r.0.0"):
                    return os.path.join(root, file)
        return None

    mca_file = find_path(tempfile.gettempdir())
    mca_file = mca_file if mca_file != None else 'r.0.0.mca'

    world_folder = args.w
    s = args.s if args.s != None else '-64:bedrock;-63:dirt;-62:dirt;-61:grass_block'

    with open(args.b, 'r') as file:
        content = file.read()
    blocklist = ast.literal_eval(content)

    Layer_of_blocks = {}
    for pair in s.split(';'):
        key, value = pair.split(':')
        Layer_of_blocks[key] = value

    SuperflatEdit(world_folder=world_folder, Layer_of_blocks=Layer_of_blocks, blocklist=blocklist, mca_file=mca_file)
