import aoc_helper

real_raw = aoc_helper.fetch(8, 2021)
test_raw = """
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
""".strip()

raw = real_raw


def parse_raw():
    rs = []
    for l in raw.splitlines():
        rs.append(l.split("|")[1].strip())
    return [x.split(" ") for x in rs]


def part_one():
    data = parse_raw()
    c = 0
    for l in data:
        for w in l:
            if len(w) in [2, 3, 4, 7]:
                c += 1

    return c


def parse_raw_2():
    rs = []
    for l in raw.splitlines():
        a, b = l.split("|")
        rs.append((a.strip(), b.strip()))
    return rs


def solve_sixes(M: dict[int, set[str]], x: set[str], y: set[str], z: set[str]):
    zero = None
    six = None
    nine = None
    ss = [x, y, z]
    for s1 in ss:
        for s2 in ss:
            if s1 == s2:
                continue
            for s3 in ss:
                if s1 == s3:
                    continue
                if s2 == s3:
                    continue
                if len(s1 & M[4]) == 4:
                    nine = s1
                    if len(s2 & M[1]) == 2:
                        zero = s2
                        six = s3
                    else:
                        zero = s3
                        six = s2
    return zero, six, nine


def solve_fives(M: dict[int, set[str]], x: set[str], y: set[str], z: set[str]):
    two = None
    three = None
    five = None

    ss = [x, y, z]
    for s1 in ss:
        for s2 in ss:
            if s1 == s2:
                continue
            for s3 in ss:
                if s1 == s3:
                    continue
                if s2 == s3:
                    continue
                if len(s2 ^ s3) == 4:
                    three = s1
                    if len(s2 & M[4]) == 3:
                        five = s2
                        two = s3
                    else:
                        five = s3
                        two = s2
    return two, three, five


def part_two():
    data: list[str] = parse_raw_2()

    c = 0
    for l in data:
        a, b = l
        a = a.split(" ")
        fives = []
        sixes = []
        M = {}
        for w in a:
            if len(w) == 2:
                M[1] = set(w)
            if len(w) == 7:
                M[8] = set(w)
            if len(w) == 3:
                M[7] = set(w)
            if len(w) == 4:
                M[4] = set(w)
            if len(w) == 6:
                sixes.append(set(w))
            if len(w) == 5:
                fives.append(set(w))
        M[0], M[6], M[9] = solve_sixes(M, sixes[0], sixes[1], sixes[2])
        M[2], M[3], M[5] = solve_fives(M, fives[0], fives[1], fives[2])

        print("----")
        print(l)

        NM = {}
        for k, v in M.items():
            nv = "".join(list(v))
            NM[nv] = k

        print(NM)
        r = ""
        for w in b.split(" "):
            w = set(w)
            n = None
            for k, v in M.items():
                if v == w:
                    n = k
            # if n == None:
            #     print(w, M.values())
            r += str(n)
        print(r)
        c += int(r)
    return c


print("PART ONE", part_one())
print("PART TWO", part_two())
