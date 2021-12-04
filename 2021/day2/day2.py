#!/usr/bin/env python3

with open('input.txt') as f:
    data = f.read()

def part1(input_data):
    horizontal = 0
    depth = 0

    for line in input_data.splitlines():
        command, amount = line.split(' ')
        amount = int(amount)

        if command == 'forward':
            depth += amount
        elif command == 'up':
            horizontal -= amount
        elif command == 'down':
            horizontal += amount
    
    print(horizontal * depth)

def part2(input_data):
    horizontal = 0
    depth = 0
    aim = 0

    for line in input_data.splitlines():
        command, amount = line.split(' ')
        amount = int(amount)

        if command == 'forward':
            horizontal += amount
            depth += (amount * aim)
        elif command == 'up':
            aim -= amount
        elif command == 'down':
            aim += amount

    print(horizontal * depth)

if __name__ == '__main__':
    part1(data)
    part2(data)
