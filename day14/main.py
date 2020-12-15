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

def gen_addrs(addr, mask):
    addr = bin(addr)[2:].zfill(len(mask))
    masked_addr = ""
    for i, bit in enumerate(mask):
        if bit == '1' or bit == 'X':
            masked_addr += bit
        if bit == '0':
            masked_addr += addr[i]

    parts = re.findall(r'[0-1]*[X][0-1]*', masked_addr)
    assert len(''.join(parts)) == len(mask)
    addrs = []
    #print(f'M: {mask}')
    #print(f'A: {addr}')
    #print(f'V: {masked_addr}')
    for i in range(2**len(parts)):
        binrepr = bin(i)[2:].zfill(len(parts))
        outstr = ""
        for j, bindigit in enumerate(binrepr):
            outstr += parts[j].replace('X', bindigit)
        #print(f'   {outstr}')

        addrs.append(int(outstr, 2))

    return addrs

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
                finalmem[a] = val

    print(sum(finalmem.values()))

part2()