
with open("input", "r") as fd:
    program = [line.strip() for line in fd.readlines()]

def part1():
    acc = 0
    ic = 0
    ran_ics = []
    while True:
        #if ic in ran_ics:
        #    print(ic)
        #    print(acc)
        #    break
        ran_ics.append(ic)
        try:
            inst, arg = program[ic].split(" ")
        except IndexError:
            print(f'Program ended, acc {acc}')
            break
        #print(f"{ic} {inst} {arg}")
        if inst == 'nop':
            if eval("ic"+arg) >= len(program) - 1:
                print(f"Nop that would jump outside at {ic}")
            ic += 1
        elif inst == 'acc':
            acc = eval("acc"+arg)
            ic += 1
        elif inst == 'jmp':
            ic = eval("ic"+arg)

class CodeBlock:
    def __init__(self, content, idx, next):
        self.content = content
        self.idx = idx
        self.child = next
        self.parents = set()

    def add_parent(self, parent):
        self.parents.add(parent)

    def explore_parents(self):
        if len(self.parents) == 0:
            print(f"{self.idx} has no parent")
            #return list(range(self.idx, self.idx + len(self.content) + 1))
            return [self.idx]
        
        ret = []
        print(f"Block {self.idx} {[parent.idx for parent in self.parents]}")
        for parent in self.parents:
            ret += parent.explore_parents()

        return ret

blocks = {}
def part2():
    codeblock = []
    for i, line in enumerate(program):
        inst, arg = line.split(" ")
        if inst == 'jmp':
            idx = i - len(codeblock)
            codeblock.append(line)
            blocks[idx] = CodeBlock(codeblock, idx, eval("i"+arg))
            for otheridx in range(i, idx, -1):
                blocks[otheridx] = blocks[idx]
            codeblock = []
        else:
            codeblock.append(line)
    
    for block in blocks.values():
        if block.child in blocks:
            blocks[block.child].add_parent(block)
        else:
            print(f'Invalid jump to {block.child} in {block.idx}')

    orphans = blocks[596].explore_parents()
    print(orphans)

    for i, line in enumerate(program):
        inst, arg = line.split(" ")
        if inst == 'nop':
            if eval("i"+arg) in orphans:
                print(f'Found potential jump at {i}')
    


part1()
