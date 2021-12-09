from collections import defaultdict
from math import copysign
import aoc_helper

real_raw = aoc_helper.fetch(7, 2021)
test_raw = """
16,1,2,0,4,2,7,1,2,14
""".strip()

raw = real_raw


def parse_raw():
    return [int(x) for x in raw.strip().split(",")]


# Sn = 1/2 × n × (a + l)


def part_one():
    data = parse_raw()
    m = float("inf")
    for pos in set(data):
        c = 0
        for n in data:
            diff = abs(n - pos)
            c += diff
        if c < m:
            m = c
    return m


def part_two():
    data = parse_raw()
    m = float("inf")
    for pos in range(min(data), max(data)):
        print(pos)
        c = 0
        for n in data:
            diff = abs(n - pos)
            c += sum(range(diff))
        if c < m:
            m = c
            print(pos)
    return m


print("PART ONE", part_one())
print("PART TWO", part_two())
