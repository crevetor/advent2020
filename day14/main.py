import re

with open("input", "r") as fd:
    mems = [line.strip() for line in fd.readlines()]


MEM_RE = r'^mem\[(\d+)]\s=\s(\d+)$'

def maskval(mask, value):
    ormask = int(mask.replace('X', '0'), 2)
    andmask = int(mask.replace('X', '1'), 2)
    print(f'  mask : 0b{mask}')
    print(f'Ormask : {bin(ormask)}')
    print(f'Anmask : {bin(andmask)}')
    return (value | ormask) & andmask

def parse_mem(line):
    match = re.match(MEM_RE, line)
    if not match:
        raise Exception("Couldn't match RE")

    return (int(match.group(1)), int(match.group(2)))

def part1():
    finalmem = {}
    mask = ""
    for mem in mems:
        if mem.startswith("mask"):
            mask = mem.split(' = ')[1]
        else:
            addr, val = parse_mem(mem)
            finalmem[addr] = maskval(mask, val)

    print(sum(list(finalmem.values())))

def gen_min_maxes(masked_addr):
    ret = []
    parts = re.findall(r'[0-1]*[X]+[0-1]*', masked_addr)
    for i, part in enumerate(parts):
        min_part = int(part.replace('X', '0'), 2) << len(''.join(parts[i+1:]))
        max_part = int(part.replace('X', '1'), 2) << len(''.join(parts[i+1:]))
        ret.append([min_part, max_part])

    return ret

def gen_addrs(addr, mask):
    addr = bin(addr)[2:].zfill(len(mask))
    masked_addr = ""
    for i, bit in enumerate(mask):
        if bit == '1' or bit == 'X':
            masked_addr += bit
        if bit == '0':
            masked_addr += addr[i]

    #print(f'{masked_addr}')
    mins_maxes = gen_min_maxes(masked_addr)
    addrs = []
    combinations = 2**len(mins_maxes)
    binlenmax = len(bin(combinations - 1)[2:])
    for i in range(combinations):
        sum = 0
        for idx, j in enumerate(bin(i)[2:].zfill(binlenmax)):
            sum += mins_maxes[idx][int(j)]
        addrs.append(sum)

    # Generate tuple of minaddr, maxaddr
    return [(addrs[i], addrs[i+1]) for i in range(0, len(addrs), 2)]


def part2():
    finalmem = {}
    mask = ""
    for mem in mems:
        if mem.startswith("mask"):
            mask = mem.split(' = ')[1]
        else:
            addr, val = parse_mem(mem)
            addrs = gen_addrs(addr, mask)
            for a in addrs:
                for i in range(a[0], a[1]+1):
                    finalmem[i] = val


    print(sum(list(finalmem.values())))

part2()