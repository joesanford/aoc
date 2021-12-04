#!/usr/bin/env python3

def count_increments(data):
    increments = 0
    previous = data[0]
    for i in data:
        if i > previous:
            increments += 1
        previous = i
    
    return increments


if __name__ == '__main__':
    with open('input.txt') as f:
        data = f.read()

    measurements = [int(x) for x in data.splitlines()]
    windows = [sum(x) for x in zip(measurements, measurements[1:], measurements[2:])]
    print(count_increments(measurements))
    print(count_increments(windows))
