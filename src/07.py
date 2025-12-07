#Advent of Code 2025 Day 07

from tools import files
import time
import copy

def test():

    input = [

        ".......S.......",
        "...............",
        ".......^.......",
        "...............",
        "......^.^......",
        "...............",
        ".....^.^.^.....",
        "...............",
        "....^.^...^....",
        "...............",
        "...^.^...^.^...",
        "...............",
        "..^...^.....^..",
        "...............",
        ".^.^.^.^.^...^.",
        "..............."

    ]

    return input

def parse(input):

    diagram = []
    s = 0

    for line in input:
        diagram.append(list(line))

    for line in diagram:
        if "S" in line:
            s = line.index("S")
            break

    diagram[1][s] = "|"

    return diagram

def traverse(diagram):

    split = 0

    for indexy, line in enumerate(diagram):
        for indexx, char in enumerate(line):

            if indexy > 0 and indexy < len(diagram):
                if diagram[indexy-1][indexx] == "|" and char == ".":
                    diagram[indexy][indexx] = "|"
                
                if diagram[indexy-1][indexx] == "|" and char == "^":
                    diagram[indexy][indexx-1] = "|"
                    diagram[indexy][indexx+1] = "|"
                    split += 1

    return split

def timelines(diagram):

    time = 0

    line = diagram[1]
    s = line.index("|")
    diagram[1][s] = "1"

    for indexy, line in enumerate(diagram):
        for indexx, char in enumerate(line):

            if indexy > 0 and indexy < len(diagram):
                if (diagram[indexy-1][indexx]).isdigit() and char == ".":
                    diagram[indexy][indexx] = diagram[indexy-1][indexx]
                
                if diagram[indexy-1][indexx].isdigit() and char == "^":

                    if diagram[indexy][indexx-1] == ".":
                        diagram[indexy][indexx-1] = diagram[indexy-1][indexx]

                    elif diagram[indexy][indexx-1].isdigit():
                        diagram[indexy][indexx-1] = str( int(diagram[indexy][indexx-1]) + int(diagram[indexy-1][indexx]))
                        
                    if (diagram[indexy-1][indexx+1]).isdigit():
                        diagram[indexy][indexx+1] = str( int(diagram[indexy-1][indexx]) + int(diagram[indexy-1][indexx+1]))

                    else:
                        diagram[indexy][indexx+1] = diagram[indexy-1][indexx]

    for char in diagram[-1]:
        if char.isdigit():
            time += int(char)

    return time

def show(diagram):

    for line in diagram:
        print(" ".join(line))

    print()

def part1(input):

    diagram = parse(input)
    split = traverse(diagram)
    show(diagram)

    print("Part 1: {}".format(split))

def part2(input):

    diagram = parse(input)
    time = timelines(diagram)

    print("Part 2: {} ".format(time))

filename = "../input/07.txt"
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