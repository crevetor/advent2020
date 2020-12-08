allbags = {}

class Bag:
    def __init__(self, color, parent=None):
        self.color = color
        self.parents = []
        self.children = {}
        if parent is not None:
            self.parents.append(parent)

    def add_parent(self, bag):
        self.parents.append(bag)

    def add_child(self, bag, numbags):
        if bag.color in self.children:
            print(f'{bag.color} already in children of {self.color}')
        self.children[bag.color] = (bag, numbags)

    def num_bags(self):
        count = 0
        for child, numbags in self.children.values():
            #print(f"{numbags} {child.color}")
            count += numbags
            count += numbags*child.num_bags()

        #print(f"returning {count}")
        return count

    def __str__(self):
        return f"{self.color} {self.parents}"

    def __repr__(self):
        return f"{self.color} {len(self.parents)}"

with open("input", "r") as fd:
    for line in fd.readlines():
        line = line.strip()
        ourcolor, innerbags = line.split(" bags contain ")
        if ourcolor not in allbags:
            allbags[ourcolor] = Bag(ourcolor)

        for innerbag in innerbags.split(", "):
            if innerbag.startswith("no other"):
                continue
            num = int(innerbag.split(' ')[0])
            color = innerbag.split(' ', 1)[1].lstrip().rsplit(" ",1)[0]
            #print(f"Adding {color} as child of {ourcolor}")
            if color in allbags:
                allbags[color].add_parent(allbags[ourcolor])
            else:
                allbags[color] = Bag(color, allbags[ourcolor])
            
            allbags[ourcolor].add_child(allbags[color], num)


containing_bags = set()
def walk_tree(root):
    containing_bags.add(root)
    if len(root.parents) == 0:
        return

    for parent in root.parents:
        walk_tree(parent)

walk_tree(allbags["shiny gold"])
containing_bags.remove(allbags["shiny gold"])
print(len(containing_bags))

print(allbags["shiny gold"].num_bags())