from collections import defaultdict
import aoc_helper

real_raw = aoc_helper.fetch(9, 2021)
test_raw = """
2199943210
3987894921
9856789892
8767896789
9899965678
""".strip()

raw = real_raw


def parse_raw():
    return [list(map(int, list(x))) for x in raw.splitlines()]


def part_one():
    data = parse_raw()
    lows = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            c = data[i][j]
            adjs = []
            if i + 1 < len(data):
                adjs.append(data[i + 1][j])
            if i - 1 >= 0:
                adjs.append(data[i - 1][j])
            if j + 1 < len(data[0]):
                adjs.append(data[i][j + 1])
            if j - 1 >= 0:
                adjs.append(data[i][j - 1])
            ok = True
            for a in adjs:
                if a <= c:
                    ok = False
                    break
            if ok:
                lows.append(c + 1)
                print(c)
    return sum(lows)


def def_value():
    return 0


seen = {}
M = defaultdict(def_value)


def rec(i, j, data, c):
    d = data[i][j]
    if d == 9:
        return

    if not (i, j) in seen:
        c += 1

    seen[(i, j)] = True

    ok = False
    if i + 1 < len(data) and data[i + 1][j] < d:
        rec(i + 1, j, data, c)
        ok = True
    if i - 1 >= 0 and data[i - 1][j] < d:
        rec(i - 1, j, data, c)
        ok = True
    if j + 1 < len(data[0]) and data[i][j + 1] < d:
        rec(i, j + 1, data, c)
        ok = True
    if j - 1 >= 0 and data[i][j - 1] < d:
        rec(i, j - 1, data, c)
        ok = True
    if not ok:
        M[(i, j)] += c


def part_two():
    data = parse_raw()
    lows = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            c = data[i][j]
            adjs = []
            if i + 1 < len(data):
                adjs.append(data[i + 1][j])
            if i - 1 >= 0:
                adjs.append(data[i - 1][j])
            if j + 1 < len(data[0]):
                adjs.append(data[i][j + 1])
            if j - 1 >= 0:
                adjs.append(data[i][j - 1])
            ok = True
            for a in adjs:
                if a <= c:
                    ok = False
                    break
            if ok:
                lows.append((i, j))
    bs = []
    for i, j in lows:
        start = data[i][j]
        start_coord = (i, j)
        q = [(i, j, int(-1))]

        seen = {}
        c = 0
        while len(q) > 0:
            i, j, prev = q.pop(0)
            if (i, j) in seen:
                continue
            if i < 0 or i >= len(data):
                continue
            if j < 0 or j >= len(data[0]):
                continue

            d = data[i][j]
            if d == 9:
                continue
            if d <= prev:
                continue
            seen[(i, j)] = True

            c += 1
            q.append((i + 1, j, d))
            q.append((i - 1, j, d))
            q.append((i, j + 1, d))
            q.append((i, j - 1, d))
        print(start, start_coord, c)
        bs.append(c)

    bs.sort(reverse=True)

    ans = bs[0] * bs[1] * bs[2]
    print(bs)

    # for i in range(len(data)):
    #     for j in range(len(data[0])):
    #         rec(i, j, data, 0)
    return ans


print("PART ONE", part_one())
print("PART TWO", part_two())
