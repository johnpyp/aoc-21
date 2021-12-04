import aoc_helper

real_raw = aoc_helper.fetch(2, 2021)
test_raw = """
forward 5
down 5
forward 8
up 3
down 8
forward 2
""".strip()

raw = real_raw


def parse_raw():

    # lines = []
    # for line in raw.splitlines():
    #     direction, n = line.split(" ")
    #     lines.append((direction, int(n)))
    return [(line.split(" ")[0], int(line.split(" ")[1])) for line in raw.splitlines()]


data = parse_raw()


def part_one():

    posy = 0
    posx = 0
    for (d, n) in data:
        if d == "forward":
            posx += n
        if d == "down":
            posy += n
        if d == "up":
            posy -= n
    return posy * posx


def part_two():
    posy = 0
    posx = 0
    aim = 0
    for (d, n) in data:
        if d == "forward":
            posx += n
            posy += aim * n
        if d == "down":
            # posy += n
            aim += n
        if d == "up":
            # posy -= n
            aim -= n
        print(posx, posy, aim)
    return posy * posx


print("PART ONE: " + str(part_one()))
print("PART TWO: " + str(part_two()))
# aoc_helper.lazy_submit(day=2, year=2021, solution=part_one)
# aoc_helper.lazy_submit(day=2, year=2021, solution=part_two)
