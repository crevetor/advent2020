with open("input", "r") as fd:
    timestamp = int(fd.readline().strip())
    buses = [bus for bus in fd.readline().strip().split(",")]

def part1():
    best_bus = [0, timestamp]
    for bus in [int(bus) for bus in buses if bus != 'x']:
        ts = 0
        while ts < timestamp:
            ts += bus
        
        if ts - timestamp < best_bus[1]:
            best_bus = [bus, ts - timestamp]
        print(f'Bus {bus} would depart at {ts} (diff {ts - timestamp})')
    print(f'Best bus {best_bus[0]} with diff {best_bus[1]} ({best_bus[0] * best_bus[1]})')

def found(ts):
    for i, bus in enumerate(buses):
        if bus == 'x':
            continue
        if (ts + i) % int(bus) != 0:
            return False
    return True

def part2():
    max_bus = max([int(bus) for bus in buses if bus != 'x'])
    mul = int(100000000000000/max_bus) + 1
    max_bus_idx = buses.index(str(max_bus))
    ts = (mul*max_bus) - max_bus_idx
    while not found(ts):
        ts += max_bus
        if ts%10000 == 0:
            print(f'TS: {ts}')

    print(f'Found {ts}')

part2()