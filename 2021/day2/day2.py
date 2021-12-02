#!/usr/bin/env python3

with open('input.txt') as f:
    input_data = f.read()

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