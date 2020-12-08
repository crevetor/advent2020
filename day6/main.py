inputs = []

with open("input", "r") as fd:
    inputs = [line.strip() for line in fd.readlines()]


def parse_group(lines):
    out = {}
    for line in lines:
        for letter in line:
            if letter in out:
                out[letter] += 1
            else:
                out[letter] = 1

    count = 0
    for v in out.values():
        if v == len(lines):
            count += 1
    
    return count

acc_lines = []
group_counts = []
for line in inputs:
    if line == "":
        group_counts.append(parse_group(acc_lines))
        acc_lines = []
    else:
        acc_lines.append(line)

group_counts.append(parse_group(acc_lines))
print(group_counts)
print(sum(group_counts))

