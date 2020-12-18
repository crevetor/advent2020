lines = [
    '2 * 3 + (4 * 5)',
    '5 + (8 * 3 + 9 + 3 * 4 * 3)',
    '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))',
    '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'
]

lines = [
    '1 + (2 * 3) + (4 * (5 + 6))',
    '2 * 3 + (4 * 5)',
    '5 + (8 * 3 + 9 + 3 * 4 * 3)',
    '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))',
    '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'
]

with open("input", "r") as fd:
    lines = [line.strip() for line in fd.readlines()]

class Number:
    def __init__(self, num):
        self.num = int(num)

    def evaluate(self):
        return self.num

    def __str__(self):
        return str(self.num)
    
class Operator:

    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def evaluate(self):
        return eval(f"{self.left.evaluate()}  {self.operator} {self.right.evaluate()}")

    def __str__(self):
        return f'({self.operator} {self.left} {self.right})'

def remove_parentheses_if_needed(line):
    if line[0] != '(':
        return line

    parentheses = 0
    for char in line:
        if char == '(':
            parentheses += 1
            continue
        if char == ')':
            parentheses -= 1
            continue
        if parentheses == 0:
            return line

    return line[1:-1]

def split_at_root(line):
    if len(line) == 1:
        return Number(line)

    parentheses = 0
    idx = -1
    for i, char in enumerate(reversed(line)):
        if char in '+-*/' and parentheses == 0:
            idx = len(line) - 1 - i
            break
        if char == ')':
            parentheses += 1
        if char == '(':
            parentheses -= 1

    left = remove_parentheses_if_needed(line[:idx])
    right = remove_parentheses_if_needed(line[idx+1:])

    return Operator(split_at_root(left), line[idx], split_at_root(right))
    

def part1():
    total = 0
    for line in lines:
        line = line.replace(' ','')
        root = split_at_root(line)
        print(root)
        result = root.evaluate()
        print(result)
        total += result

    print(total)

def split_at_root2(line):
    if len(line) == 1:
        return Number(line)

    parentheses = 0
    idx = -1
    for i, char in enumerate(reversed(line)):
        if char == '*' and parentheses == 0:
            idx = len(line) - 1 - i
            break
        if char == '+' and parentheses == 0 and idx == -1:
            idx = len(line) - 1 - i
        if char == ')':
            parentheses += 1
        if char == '(':
            parentheses -= 1

    left = remove_parentheses_if_needed(line[:idx])
    right = remove_parentheses_if_needed(line[idx+1:])

    return Operator(split_at_root2(left), line[idx], split_at_root2(right))

def part2():
    total = 0
    for line in lines:
        line = line.replace(' ','')
        root = split_at_root2(line)
        print(root)
        result = root.evaluate()
        print(result)
        total += result

    print(total)

part2()