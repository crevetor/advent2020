from functools import reduce 

with open("input", "r") as fd:
    adapters = [int(line.strip()) for line in fd.readlines()]
    adapters.sort()

#adapters = [1, 2, 3, 4, 5, 6]

def part1():
    differences = {}
    for i, adapter in enumerate(adapters):
        if i == 0:
            diff = adapter
        else:
            diff = adapter - adapters[i-1]
        
        if diff in differences:
            differences[diff] += 1
        else:
            differences[diff] = 1

    # add the device adapter
    differences[3] += 1

    print(differences)
    print(differences[1] * differences[3])

class Node:
    def __init__(self, jolt):
        self.jolt = jolt
        self.parents = []
        self.numpaths = -1

    def isCompatible(self, otherjolt):
        return self.jolt - otherjolt.jolt > 0 and self.jolt - otherjolt.jolt < 4

    def addParent(self, otherjolt):
        self.parents.append(otherjolt)

    def numPaths(self):
        """
        Number of paths to this node
        """
        if self.numpaths > -1:
            return self.numpaths

        if self.jolt == 0:
            return 1

        paths = 0
        for parent in self.parents:
            paths += parent.numPaths()
        
        return paths
    
    def cachePaths(self):
        self.numpaths = self.numPaths()

    def hasParents(self):
        return len(self.parents) > 0

    def __str__(self):
        return f'Node {self.jolt} : {len(self.parents)} parents'

def part2():
    print(adapters)
    nodes = [Node(0)]
    for adapter in adapters:
        node = Node(adapter)
        for othernode in nodes:
            if node.isCompatible(othernode):
                node.addParent(othernode)
        if len(node.parents) == 1:
            node.cachePaths()
        nodes.append(node)
    
    print(nodes[-1].numPaths())

part2()