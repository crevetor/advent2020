import numpy as np

with open("input", "r") as fd:
    first_slice = [line.strip() for line in fd.readlines()]

CHAR_TO_INT = {
    '#': 1,
    '.': 0
}

def gen_cube(coords):
    return [slice(max(coord-1, 0), coord+2) for coord in coords]

def cycle(pocket):
    newpocket = np.copy(pocket)
    it = np.nditer(pocket, flags=['multi_index'])
    for elt in it:
        cur_idx = it.multi_index
        cube = gen_cube(cur_idx)

        surrounding_cube = pocket[cube]
        num_active = surrounding_cube.sum()

        if  elt == 1 and (num_active not in [3,4]):
            newpocket[it.multi_index] = 0 
        if elt == 0 and (num_active == 3):
            newpocket[it.multi_index] = 1
    
    return newpocket

def print_layers(pocket):
    print('-------------')
    numlayers = len(pocket)
    for i, layer in enumerate(pocket):
        if layer.sum() > 0:
            print(f'Layer {i - numlayers//2}')
            for row in layer:
                if row.sum() > 0:
                    for elt in row:
                        print(f'{"#" if elt else "."}', end='')
                    print()

def part1():
    numcycles = 6
    numlayers = numcycles*3+1
    numrows = len(first_slice) + numcycles*3
    numcols = len(first_slice[0]) + numcycles*3
    pocket = np.zeros((numlayers, numrows, numcols),  dtype=int)
    for y, line in enumerate(first_slice):
        for x, char in enumerate(line):
            pocket[numlayers//2, numrows//2+y, numcols//2+x] = CHAR_TO_INT[char]

    for cycleidx in range(numcycles):
        pocket = cycle(pocket)
        print_layers(pocket)

    print(pocket.sum())

def part2():
    numcycles = 6
    numlayers = numcycles*3+1
    numrows = len(first_slice) + numcycles*3
    numcols = len(first_slice[0]) + numcycles*3
    pocket = np.zeros((numlayers, numlayers, numrows, numcols),  dtype=int)
    for y, line in enumerate(first_slice):
        for x, char in enumerate(line):
            pocket[numlayers//2, numlayers//2, numrows//2+y, numcols//2+x] = CHAR_TO_INT[char]

    for cycleidx in range(numcycles):
        pocket = cycle(pocket)
        #print_layers(pocket)

    print(pocket.sum())

part2()