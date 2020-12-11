from copy import deepcopy

with open("input", "r") as fd:
    emptylayout = [list(line.strip()) for line in fd.readlines()]


class DifferentException(Exception):
    pass

def print_layout(layout):
    print('------------------------')
    for line in layout:
        print(''.join(line))
    print('------------------------')

def update_layout(layout):
    newlayout = deepcopy(layout)
    for y in range(len(layout)):
        for x in range(len(layout[0])):
            if layout[y][x] == '.':
                continue
            min_x = max(0, x-1)
            max_x = min(len(layout[0]), x+2)
            min_y = max(0, y-1)
            max_y = min(len(layout), y+2)
            num_occupied = 0
            for y1 in layout[min_y:max_y]:
                num_occupied += y1[min_x:max_x].count("#")
            if layout[y][x] == 'L' and num_occupied == 0:
                newlayout[y][x] = '#'
            if layout[y][x] == '#' and num_occupied > 4:
                newlayout[y][x] = 'L'
    return newlayout

def occupied_in_visible_seats_list(layout, x, y):
    num_occ = 0
    for pos in reversed(layout[y][:x]):
        if pos == 'L':
            break
        if pos == '#':
            num_occ += 1
            break
    for pos in layout[y][x+1:]:
        if pos == 'L':
            break
        if pos == '#':
            num_occ += 1
            break

    for diag in [(-1,-1), (1, -1), (1, 1), (-1, 1)]:
        x1 = x + diag[0]
        y1 = y + diag[1]
        while x1 > -1 and y1 > -1 and x1 < len(layout[0]) and y1 < len(layout):
            if layout[y1][x1] == 'L':
                break
            if layout[y1][x1] == '#':
                num_occ += 1
                break
            x1 += diag[0]
            y1 += diag[1]
    
    for row in reversed(layout[:y]):
        if row[x] == 'L':
            break
        if row[x] == '#':
            num_occ += 1
            break

    for row in layout[y+1:]:
        if row[x] == 'L':
            break
        if row[x] == '#':
            num_occ += 1
            break

    return num_occ

def update_layout_part2(layout):
    newlayout = deepcopy(layout)
    for y in range(len(layout)):
        for x in range(len(layout[0])):
            if layout[y][x] == '.':
                continue
            num_occupied = occupied_in_visible_seats_list(layout, x, y)
            if layout[y][x] == 'L' and num_occupied == 0:
                newlayout[y][x] = '#'
            if layout[y][x] == '#' and num_occupied > 4:
                newlayout[y][x] = 'L'
    return newlayout

def part1():
    layout = emptylayout
    i = 1
    while True:
        oldlayout = layout
        layout = update_layout(layout)
        try:
            for y, line in enumerate(layout):
                for x, col in enumerate(layout[y]):
                    if col != oldlayout[y][x]:
                        print(f"Layouts are different")
                        raise DifferentException
        except DifferentException:
            i += 1
            continue
        print(f'Found same layout after {i} rounds')
        break

    occupied = 0
    for line in layout:
        occupied += line.count('#')
    print(occupied)

def part2():
    layout = emptylayout
    i = 1
    while True:
        oldlayout = layout
        layout = update_layout_part2(layout)
        print_layout(layout)
        try:
            for y, line in enumerate(layout):
                for x, col in enumerate(layout[y]):
                    if col != oldlayout[y][x]:
                        print(f"Layouts are different")
                        raise DifferentException
        except DifferentException:
            i += 1
            continue
        print(f'Found same layout after {i} rounds')
        break

    occupied = 0
    for line in layout:
        occupied += line.count('#')
    print(occupied)

part2()
                
            
