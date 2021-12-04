#!/usr/bin/env python3
from collections import Counter

def part1():
    with open('input.txt') as f:
        data = [l.strip() for l in f]

    gamma = ''
    epsilon = ''
    for i in range(len(data[0])): 
        x = ''
        for d in data:
            x += d[i]

        gamma += Counter(x).most_common()[0][0]
        epsilon += Counter(x).most_common()[1][0]

    print(int(gamma, 2) * int(epsilon, 2))


def part2():
    with open('input.txt') as f:
        data = [l.strip() for l in f]
    
    o2_rating = get_rating(data, 0, 1)
    co2_rating = get_rating(data, 1, 0)

    print(o2_rating * co2_rating)

def get_rating(data, value, swap):
    counters = update_counters(data)
    for i in range(len(data[0])):
        data = filter_data(data, counters, i, value, swap)
        if len(data) == 1:
            break
        counters = update_counters(data)

    return int(data[0], 2)

def filter_data(data, counters, idx, min_max, swap):
    res = []
    for d in data:
        current = list(d)[idx]
        most_common = counters[idx].most_common()
        if min_max >= len(most_common):
            continue
        if most_common[0][1] == most_common[1][1] and int(current) == swap:
            res.append(d)
        elif most_common[0][1] != most_common[1][1] and current == most_common[min_max][0]:
            res.append(d)

    return res if res else data

def update_counters(data):
    counters = [Counter() for _ in range(len(data[0]))]
    for d in data:
        for idx, c in enumerate(list(d)):
            counters[idx].update(c)
    
    return counters

part1()
part2()
