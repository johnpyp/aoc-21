from collections import defaultdict
from math import copysign
import aoc_helper

real_raw = aoc_helper.fetch(6, 2021)
test_raw = """
3,4,3,1,2
""".strip()

raw = real_raw


def parse_raw():
    return [int(x) for x in raw.strip().split(",")]


def evolve(start, n, M):
    if (start, n) in M:
        return M[(start, n)]
    r = 0
    if n == 0:
        r = 1
    else:
        next_start = 6 if start == 0 else start - 1
        r += evolve(next_start, n - 1, M)
        if start == 0:
            r += evolve(8, n - 1, M)
    M[(start, n)] = r
    return r


def part_one():
    data = parse_raw()
    M = {}
    c = 0
    for n in data:
        c += evolve(n, 80, M)

    return c


def part_two():
    data = parse_raw()
    M = {}
    c = 0
    for n in data:
        c += evolve(n, 256, M)

    return c
    return -1


print("PART ONE", part_one())
print("PART TWO", part_two())
