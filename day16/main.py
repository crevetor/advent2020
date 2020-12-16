from collections import Counter

with open("input", "r") as fd:
    lines = [line.strip() for line in fd.readlines()]

mode = "fields"
fields = {}
my_ticket = []
other_tickets = []
for line in lines:
    if line == '':
        continue
    if line == 'your ticket:':
        mode = 'myticket'
        continue
    if line == 'nearby tickets:':
        mode = 'othertickets'
        continue

    if mode == 'fields':
        name, val = line.split(': ')
        fields[name] = [list(map(lambda x: int(x), range.split("-"))) for range in val.split(' or ')]
    if mode == 'myticket':
        my_ticket = [int(i) for i in line.split(",")]
    if mode == 'othertickets':
        other_tickets.append([int(i) for i in line.split(",")])

def value_is_valid(value):
    for fieldranges in fields.values():
        for range in fieldranges:
            if value >= range[0] and value <= range[1]:
                return True
    
    return False

def part1():
    invalid_values = []
    for ticket in other_tickets:
        for value in ticket:
            if not value_is_valid(value):
                print(f'{value} is invalid')
                invalid_values.append(value)
    
    print(sum(invalid_values))

class Ticket:
    def __init__(self, values):
        self.is_valid = True
        self.possible_fields = {}
        for i, value in enumerate(values):

            possible_fields = []
            for field in fields.keys():
                if self.valid_for_field(field, value):
                    possible_fields.append(field)

            if len(possible_fields) == 0:
                self.is_valid = False
                break
            else:
                self.possible_fields[i] = possible_fields

    def valid_for_field(self, field, value):
        for range in fields[field]:
            if value >= range[0] and value <= range[1]:
                return True
        return False
    
    def __str__(self):
        return str(self.possible_fields)

def part2():
    tick_objs = []
    for ticket in other_tickets:
        tick_objs.append(Ticket(ticket))

    final_guesses = {}
    for ticket in tick_objs:
        if ticket.is_valid:
            for idx in ticket.possible_fields:
                if len(ticket.possible_fields[idx]) == 1:
                    print(f'Only one possible field for {idx}: {ticket.possible_fields[idx]}')
                if idx in final_guesses:
                    final_guesses[idx] += ticket.possible_fields[idx]
                else:
                    final_guesses[idx] = ticket.possible_fields[idx]

    numvalids = len([obj for obj in tick_objs if obj.is_valid])
    finalfields = {}
    usedfields = []
    while len(finalfields) != len(my_ticket):
        for idx, guesses in final_guesses.items():
            if idx in finalfields:
                continue
            allagree = []
            for guess, count in Counter(guesses).items():
                if guess in usedfields:
                    continue
                if count == numvalids:
                    allagree.append(guess)
            
            if len(allagree) == 1:
                print(f'Found {allagree[0]} at idx {idx}')
                usedfields.append(allagree[0])
                finalfields[idx] = allagree[0]
    
    print(finalfields)
    prod = 1
    for idx, value in finalfields.items():
        if value.startswith('departure'):
            prod *= my_ticket[idx]
    print(prod)

part2()
