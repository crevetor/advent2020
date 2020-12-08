import re

class Passport:
    mandatory_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    optional_field = ['cid']

    def __init__(self, inputstrings):
        self.elements = {}
        for line in inputstrings:
            for elt in line.split(' '):
                k, v = elt.split(':')
                if k in self.elements:
                    print(f'{k} already in elements {self.elements}')
                self.elements[k] = v

    def isValid(self):
        for field in self.mandatory_fields:
            if field not in self.elements:
                return False
        
        for field in ['byr', 'iyr', 'eyr']:
            if len(self.elements[field]) != 4:
                return False

        try:
            byr = int(self.byr)
            iyr = int(self.iyr)
            eyr = int(self.eyr)
        except ValueError:
            return False

        if byr < 1920 or byr > 2002:
            return False
        
        if iyr < 2010 or iyr > 2020:
            return False

        if eyr < 2020 or eyr > 2030:
            return False

        hgt_re = r'^[0-9]+(cm|in)$'
        if not re.match(hgt_re, self.hgt):
            print(f"{self.hgt} did not match re")
            return False

        if self.hgt.endswith('cm'):
            height = int(self.hgt[:-2])
            if height < 150 or height > 193:
                return False
        
        if self.hgt.endswith('in'):
            height = int(self.hgt[:-2])
            if height < 59 or height > 76:
                return False

        hcl_re = r'^#[0-9a-f]{6}$'
        if not re.match(hcl_re, self.hcl):
            print(f"{self.hcl} did not match re")
            return False

        if self.ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            print(f"{self.ecl} is not a valid eye color")
            return False

        pid_re = r'^[0-9]{9}$'
        if not re.match(pid_re, self.pid):
            print(f"{self.pid} did not match re")
            return False

        return True

    def __getattr__(self, attr):
        if attr in self.elements:
            return self.elements[attr]
        
        raise AttributeError

    def debug(self):
        print(f'Num fields : {len(self.elements)}')
        print(self.isValid())
        print(sorted(list(self.elements.keys())))


passports = []
with open('input', 'r') as fd:
    lines = fd.readlines()
    acclines = []
    for line in lines:
        if line.strip() == '':
            passports.append(Passport(acclines))
            acclines = []
        else:
            acclines.append(line.strip())
    passports.append(Passport(acclines))

for passport in passports:
        passport.debug()
        print('---------------------------------')

valids = list(filter(lambda x: x.isValid(), passports))
print(len(valids))