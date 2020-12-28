import numpy as np
import sys

with open("input_part2", "r") as fd:
    lines = [line.strip() for line in fd.readlines()]

CHAR_TO_INT = {
    '.': 0,
    '#': 1
}

SEE_MONSTER= [
    "..................#.",
    "#....##....##....###",
    ".#..#..#..#..#..#..."
]

image = np.array([[CHAR_TO_INT[char] for char in line] for line in lines])
see_monster = np.array([[CHAR_TO_INT[char] for char in line] for line in SEE_MONSTER])

for flip in range(-1, 2):
    for rotate in range(4):
        newimage = np.copy(image)
        if flip > -1:
            newimage = np.flip(newimage, flip)
        newimage = np.rot90(newimage, rotate, (1,0))
        #print(f'Rot {rotate*90}, Flip : {flip}')
        #print(newimage)
        num_monsters = 0
        for y in range(len(image) - len(see_monster)): 
            for x in range(len(image[0]) - len(see_monster[0])):
                res = newimage[y:y+len(see_monster), x:x+len(see_monster[0])]*see_monster
                if np.sum(res) == np.sum(see_monster):
                    print(f'Found monster at {x} {y}')
                    num_monsters += 1
        if num_monsters > 0:
            roughness = np.sum(image) - num_monsters*np.sum(see_monster)
            print(roughness)
            sys.exit(0)
