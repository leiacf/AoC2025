#Advent of Code 2025 Day 03

from tools import files
import time
import itertools

def test():

    input = [

        "987654321111111",
        "811111111111119",
        "234234234234278",
        "818181911112111"

    ]

    return input

def parse(input, length):

    answer = 0

    for bank in input:

        number = ""

        for x in range(length-1, -1, -1):

            if x == 0:
                digit = max(bank)
            else:
                digit = max(bank[ : -x])

            bank = bank[bank.index(digit)+1 : ]
            number += digit

        answer += int(number)

    return answer

def part1(input):

    answer = parse(input, 2)

    print("Part 1: {}".format(answer))


def part2(input):

    answer = parse(input, 12)
    
    print("Part 2: {} ".format(answer))

filename = "../input/03.txt"
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