import aoc_helper

real_raw = aoc_helper.fetch(3, 2021)
test_raw = """
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
""".strip()

raw = real_raw


def parse_raw():
    return [line for line in raw.splitlines()]


data = parse_raw()


def part_one():

    r1 = ""
    r2 = ""
    for i in range(len(data[0])):
        ones = 0
        zeroes = 0
        for j in range(len(data)):
            n = int(data[j][i])
            if n == 1:
                ones += 1
            if n == 0:
                zeroes += 1
        if ones > zeroes:
            r1 += "1"
            r2 += "0"
        else:
            r1 += "0"
            r2 += "1"
    n1 = int(r1, 2)
    n2 = int(r2, 2)

    return n1 * n2


def filtermemes(arr: list[str], i, gt):
    while True:
        ones = 0
        zeroes = 0
        for ns in arr:
            bit = int(ns[i])
            if bit == 1:
                ones += 1
            if bit == 0:
                zeroes += 1
        last_len = len(arr)
        # print(gt, ones, zeroes, arr)
        if ones == zeroes:
            if gt:
                arr = list(filter(lambda ns: ns[i] == "1", arr))
            else:
                arr = list(filter(lambda ns: ns[i] == "0", arr))
        elif ones > zeroes:
            if gt:
                arr = list(filter(lambda ns: ns[i] == "1", arr))
            else:
                arr = list(filter(lambda ns: ns[i] == "0", arr))
        else:
            if gt:
                arr = list(filter(lambda ns: ns[i] == "0", arr))
            else:
                arr = list(filter(lambda ns: ns[i] == "1", arr))

        return arr


def do_filter(poggers, gt):
    for i in range(len(poggers[0])):
        print(poggers)
        poggers = filtermemes(poggers, i, gt)
        if len(poggers) == 1:
            break
    return int(poggers[0], 2)


def part_two():
    oxygen = do_filter(data, True)
    co2 = do_filter(data, False)
    # arr1 = data
    # for i in range(len(arr1[0])):
    #     print(arr1)
    #     arr1 = filtermemes(arr1, i, True)
    # oxygen = int(arr1[0], 2)
    # print(oxygen)
    # arr2 = data
    # for j in range(len(arr2[0])):
    #     print(arr2)
    #     arr2 = filtermemes(arr2, j, False)
    # co2 = int(arr2[0], 2)
    return oxygen * co2

    # d1 = data.copy()
    # d2 = data.copy()
    # while True:
    # for i in range(len(data[0])):
    #     ones = 0
    #     zeroes = 0
    #     for j in range(len(data)):
    #         n = int(data[j][i])
    #         if n == 1:
    #             ones += 1
    #         if n == 0:
    #             zeroes += 1
    #     if ones > zeroes:
    #         r1.append(1)
    #         r2.append(0)
    #     else:
    #         r1.append(0)
    #         r2.append(1)


print("PART ONE: " + str(part_one()))
print("PART TWO: " + str(part_two()))
# aoc_helper.lazy_submit(day=2, year=2021, solution=part_one)
# aoc_helper.lazy_submit(day=2, year=2021, solution=part_two)
