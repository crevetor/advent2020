import numpy as np
import re

with open("input", "r") as fd:
    lines = [line.strip() for line in fd.readlines()]

TILE_RE=r'^Tile (\d+):$'

class Tile:

    def __init__(self, id, content):
        self.id = id
        self.content = np.array([list(a) for a in content])
        self.orientationValid = False
        self.rot = 0
        self.flip = (0, 0)
        self.edges = set([''.join(a) for a in [
            self.content[0], list(reversed(self.content[0])),
            self.content[...,-1], list(reversed(self.content[..., -1])),
            self.content[-1], list(reversed(self.content[-1])),
            self.content[...,0], list(reversed(self.content[...,0]))
        ]])
        self.adjascent_tiles = set()

    def matchEdges(self, other):
        common_edges = list(self.edges.intersection(other.edges))
        if len(common_edges) >= 1:
            print(f"Found matching edge between {self.id} and {other.id}")
            print(common_edges[0])
            self.adjascent_tiles.add(other.id)

def part1():
    tile_id = -1
    acc = []
    tileobjs = []
    for line in lines:
        match = re.match(TILE_RE, line)
        if match:
            tile_id = match.group(1)
            continue
        if line == '':
            tileobjs.append(Tile(tile_id, acc))
            acc = []
            continue
        acc.append(line)
    tileobjs.append(Tile(tile_id, acc))

    for i, tileobj in enumerate(tileobjs):
        for j, otherobj in enumerate(tileobjs):
            if i != j:
                tileobj.matchEdges(otherobj)
    
    prod = 1
    for tileobj in tileobjs:
        if len(tileobj.adjascent_tiles) == 2:
            print(f'Tile {tileobj.id} is a corner')
            prod *= int(tileobj.id)
    print(prod)

part1()
        
