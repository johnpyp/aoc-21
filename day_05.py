from collections import defaultdict
from math import copysign
import aoc_helper

real_raw = aoc_helper.fetch(5, 2021)
test_raw = """
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
""".strip()

raw = real_raw


def parse_raw():
    segments = []
    for line in raw.splitlines():
        p1, p2 = line.split(" -> ")
        x1, y1 = [int(x) for x in p1.split(",")]
        x2, y2 = [int(x) for x in p2.split(",")]
        segments.append(((x1, y1), (x2, y2)))

    return segments


def progress(source, target):
    if source >= target:
        return -1
    return 1


def default_value():
    return 0


def draw_line(p1, p2, M, diag=False):
    x1, y1 = p1
    x2, y2 = p2
    if x1 != x2 and y1 != y2 and not diag:
        return
    if x1 != x2 and y1 != y2:
        while x1 != x2 and y1 != y2:
            M[(x1, y1)] += 1
            x1 += progress(x1, x2)
            y1 += progress(y1, y2)
        M[(x1, y1)] += 1
    else:
        if x1 != x2:
            while x1 != x2:
                M[(x1, y1)] += 1
                x1 += progress(x1, x2)
            M[(x1, y1)] += 1

        if y1 != y2:
            while y1 != y2:
                M[(x1, y1)] += 1
                y1 += progress(y1, y2)
            M[(x1, y1)] += 1


def part_one():
    data = parse_raw()

    M = defaultdict(default_value)
    for (p1, p2) in data:
        draw_line(p1, p2, M)

    c = 0
    for (k, v) in M.items():
        if v > 1:
            c += 1
    return c


def part_two():
    data = parse_raw()
    M = defaultdict(default_value)
    for (p1, p2) in data:
        draw_line(p1, p2, M, True)

    c = 0
    for (k, v) in M.items():
        if v > 1:
            c += 1
    return c


print("PART ONE", part_one())
print("PART TWO", part_two())
