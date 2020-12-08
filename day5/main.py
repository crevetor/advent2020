with open("input", "r") as fd:
    bpasses = [line.strip() for line in fd.readlines()]


def get_row(binput):
    rows = list(range(128))
    for letter in binput:
        if letter == 'F':
            rows = rows[:int(len(rows)/2)]
        elif letter == 'B':
            rows = rows[int(len(rows)/2):]
    print(f'Len : {len(rows)} val {rows[0]}')
    return rows[0]

def get_col(binput):
    columns = list(range(8))
    for letter in binput:
        if letter == 'L':
            columns = columns[:int(len(columns)/2)]
        elif letter == 'R':
            columns = columns[int(len(columns)/2):]
    print(f'COL: Len {len(columns)} val {columns[0]}')
    return columns[0]

allids = []
max_id=0
for line in bpasses:
    row = get_row(line[:7])
    col = get_col(line[7:])
    bpassid = row*8 + col
    print(f'Id : {bpassid}')
    max_id = max(bpassid, max_id)
    allids.append(bpassid)

print(f'Max id : {max_id}')
allids.sort()
print(allids)
for i, curid in enumerate(allids):
    nextid = curid + 1
    nextvalidid = allids[i+1]
    if nextid != nextvalidid:
        print(f'Our id is {nextid}')
        break