import re

MAX_CALLS = 20

with open("input", "r") as fd:
    lines = [line.strip() for line in fd.readlines()]

class Rule:

    def __init__(self, idx, rule):
        self.numcalls = 0
        self.idx = idx
        self.children = {}
        if '"' in rule:
            self.rule = rule.strip('"')
            self.hasDependency = False
        else:
            self.rule = rule
            self.hasDependency = True
    
    @property
    def dependencies(self):
        return set(map(int, re.findall(r'\d+', self.rule)))

    def addChildRule(self, rule):
        self.children[rule.idx] = rule

    def render(self):
        rendered = "(" if self.hasDependency else ""
        for char in self.rule.split(' '):
            if char.isdigit():
                if int(char) != self.idx:
                    rendered += self.children[int(char)].render()
                else:
                    if self.numcalls > MAX_CALLS:
                        return ""
                    else:
                        self.numcalls += 1
                        rendered += self.children[int(char)].render()
            else:
                rendered += char
        return rendered + ")" if self.hasDependency else rendered

def parse_rules(rule_lines):
    ruleobjs = {}
    for line in rule_lines:
        idx, rule = line.split(': ')
        ruleobjs[int(idx)] = (Rule(int(idx), rule))

    for rule in ruleobjs.values():
        for dep in rule.dependencies:
            rule.addChildRule(ruleobjs[dep])

    return f"^{ruleobjs[0].render()}$"

def part1():
    rules = []
    for breakidx, line in enumerate(lines):
        if line == '':
            break
        rules.append(line)
    
    regex = parse_rules(rules)
    print(regex)
    count = 0
    for line in lines[breakidx:]:
        if re.fullmatch(regex, line):
            count += 1
            print(line)

    print(f"{count} lines match")

part1()