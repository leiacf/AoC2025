#Advent of Code 2025 Day 00

from tools import files
import time

def test():

    input = [


    ]

    return input

def part1(input):

    print("Part 1: {}".format(input))


def part2(input):

    print("Part 2: {} ".format(input))

filename = "../input/test.txt"
input = files.input_as_string(filename)
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