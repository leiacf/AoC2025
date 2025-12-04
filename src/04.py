#Advent of Code 2025 Day 04

from tools import files
import time

def test():

    input = [

        "..@@.@@@@.",
        "@@@.@.@.@@",
        "@@@@@.@.@@",
        "@.@@@@..@.",
        "@@.@@@@.@@",
        ".@@@@@@@.@",
        ".@.@.@.@@@",
        "@.@@@.@@@@",
        ".@@@@@@@@.",
        "@.@.@@@.@."

    ]

    return input

def parse(input):

    data = {}
    y = 0

    for line in input:

        for index, spot in enumerate(line):

            data[index, y] = spot

        y += 1

    return data

def calculate(data):

    answer = 0

    for key, value in data.items():

        if value == "@":

            neighbours = check(key, data)

            if neighbours <=3:
                answer += 1

    return answer

def remove(data):

    answer = 0

    while True:

        removable = []

        for key, value in data.items():

            if value == "@":

                neighbours = check(key, data)

                if neighbours <=3:
                    removable.append(key)
                    answer += 1

        for key in removable:
            del data[key]

        if len(removable) == 0:
            break

    return answer

def check(point, data):

    x, y = point
    checks = []
    count = 0

    w = (x-1, y)
    checks.append(w)

    nw = (x-1, y-1)
    checks.append(nw)
    
    n = (x, y-1)
    checks.append(n)
    
    ne = (x+1, y-1)
    checks.append(ne)
    
    e = (x+1, y)
    checks.append(e)
    
    se = (x+1, y+1)
    checks.append(se)
    
    s = (x, y+1)
    checks.append(s)
    
    sw = (x-1, y+1)
    checks.append(sw)

    for c in checks:
        if c in data:
            if data[c] == "@":
                count += 1
 
    return count

def part1(input):

    data = parse(input)

    answer = calculate(data)

    print("Part 1: {}".format(answer))


def part2(input):

    data = parse(input)
    answer = remove(data)

    print("Part 2: {} ".format(answer))

filename = "../input/04.txt"
input = files.input_as_list(filename)
#input = test()

print()

start1 = time.perf_counter()
part1(input)
end1 = time.perf_counter()

start2 = time.perf_counter()
part2(input)
end2 = time.perf_counter()

print()
print("Spent {:>7.3f} seconds on Part 1".format(end1-start1))
print("Spent {:>7.3f} seconds on Part 2".format(end2-start2))