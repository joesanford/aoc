#!/usr/bin/env python3

def count_increments(input_data):
    increments = 0
    previous = input_data[0]
    for i in input_data:
        if i > previous:
            increments += 1
        previous = i
    
    return increments

with open('input.txt') as f:
    input_data = f.read()

measurements = [int(x) for x in input_data.splitlines()]
windows = [sum(x) for x in zip(measurements, measurements[1:], measurements[2:])]
print(count_increments(measurements))
print(count_increments(windows))
