test_input = [0,3,6]
input = [11,18,0,20,1,7,16]

def last_indices(turns, number):
    indices = []
    for i, num in enumerate(reversed(turns)):
        if number == num:
            indices.append(len(turns)-i)
            if len(indices) == 2:
                break
    return indices

def part1():
    turns = input
    i = len(turns)
    while i < 2020:
        num = turns[-1]
        if turns.count(num) == 1:
            turns.append(0)
        else:
            indices = last_indices(turns, num)
            turns.append(indices[0] - indices[1])
        #print(f'{i} {turns}')
        
        i += 1

    print(turns[-1])

def part2(part_input):
    appearances = {}
    for idx, num in enumerate(part_input):
        if num not in appearances:
            appearances[num] = [idx]
        else:
            appearances[num].append(idx)

    i = len(part_input)
    num = part_input[-1]
    while i < 30000000:
        if num in appearances and len(appearances[num]) == 1:
            num = 0
            appearances[0].append(i)
        else:
            newnum = appearances[num][-1] - appearances[num][-2]
            if newnum in appearances:
                appearances[newnum].append(i)
            else:
                appearances[newnum] = [i]
            num = newnum
        #print(f'{i} {turns}')
        
        i += 1

    print(num)
        
part2(input)