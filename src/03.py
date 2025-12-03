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

def getNumbers(input):

    data = []

    for bank in input:
        
        numbers = []

        combinations = list(itertools.combinations(bank,2))
        
        for pair in combinations:

            number = int("".join(pair))
            numbers.append(number)

        numbers.sort(reverse = True)

        data.append(numbers[0])

    return data

def calculate(data):

    answer = 0

    for number in data:
        answer += number

    return answer


def part1(input):

    data = getNumbers(input)

    answer = calculate(data)

    print("Part 1: {}".format(answer))


def part2(input):

    print("Part 2: {} ".format(""))

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