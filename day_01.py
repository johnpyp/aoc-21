import aoc_helper

# raw = """199
# 200
# 208
# 210
# 200
# 207
# 240
# 269
# 260
# 263
# """
raw = aoc_helper.fetch(1, 2021)


def parse_raw():
    return [int(line) for line in raw.strip().splitlines()]


data = parse_raw()


def part_one():
    increases = 0
    last = float("inf")
    for n in data:
        if n > last:
            increases += 1
        last = n
    return increases


def part_two():
    increases = 0
    last = float("inf")
    for i in range(len(data)):
        n1 = data[i]
        n2 = data[i + 1]
        n3 = data[i + 2]
        s = n1 + n2 + n3
        if s > last:
            increases += 1
        last = s
    return increases


# print(part_one())
# aoc_helper.lazy_submit(day=1, year=2021, solution=part_one)
print(part_two())
aoc_helper.lazy_submit(day=1, year=2021, solution=part_two)
