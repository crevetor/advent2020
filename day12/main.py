import math

with open("input", "r") as fd:
    directions = [line.strip() for line in fd.readlines()]

angle_to_direction = {
    0: 'N',
    90: 'E',
    180: 'S',
    270: 'W',
    360: 'N'
}

direction_to_displacement = {
    'N': (1, 0),
    'S': (-1, 0),
    'E': (0, -1),
    'W': (0, 1)
}

class Ship:
    def __init__(self):
        self.position = [0, 0]
        self.orientation = 90

    def turn(self, direction, angle):
        if direction == 'R':
            self.orientation = (self.orientation + angle)%360
        elif direction == 'L':
            self.orientation = (self.orientation - angle)%360

        print(f'New orientation {self.orientation} ({angle_to_direction[self.orientation]})')

    def move(self, direction, units):
        if direction == 'F':
            direction = angle_to_direction[self.orientation]
        
        disp = direction_to_displacement[direction]
        self.position[0] = self.position[0] + units*disp[0]
        self.position[1] = self.position[1] + units*disp[1]

        print(f'New position {self.position}')

    def get_distance(self):
        return abs(self.position[0]) + abs(self.position[1])

class Ship2(Ship):
    def __init__(self):
        super().__init__()
        self.waypoint = [1, -10]

    def turn(self, direction, angle):
        sign = 1
        if direction == 'L':
            sign = -1
        angle = math.radians(sign*angle)
        x = self.waypoint[1]
        y = self.waypoint[0]
        self.waypoint[1] = round(math.cos(angle)*x - math.sin(angle)*y)
        self.waypoint[0] = round(math.sin(angle)*x + math.cos(angle)*y)
        print(f'New waypoint position : {self.waypoint}')
        
    def moveShip(self, units):
        self.position[0] = self.position[0] + units*self.waypoint[0]
        self.position[1] = self.position[1] + units*self.waypoint[1]
        print(f'New ship position : {self.position}')

    def moveWaypoint(self, direction, units):
        disp = direction_to_displacement[direction]
        self.waypoint[0] = self.waypoint[0] + units*disp[0]
        self.waypoint[1] = self.waypoint[1] + units*disp[1]
        print(f'New waypoint position : {self.waypoint}')

    def move(self, direction, units):
        if direction == 'F':
            self.moveShip(units)
        else:
            self.moveWaypoint(direction, units)

def part1():
    ship = Ship()
    for direction in directions:
        print(direction)
        inst = direction[0]
        val = int(direction[1:])
        if inst in ['R', 'L']:
            ship.turn(inst, val)
        else:
            ship.move(inst, val)

    print(ship.position)
    print(ship.get_distance())

def part2():
    ship = Ship2()
    for direction in directions:
        print(direction)
        inst = direction[0]
        val = int(direction[1:])
        if inst in ['R', 'L']:
            ship.turn(inst, val)
        else:
            ship.move(inst, val)

    print(ship.position)
    print(ship.get_distance())

part2()