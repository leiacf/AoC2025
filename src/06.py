#Advent of Code 2025 Day 06

from tools import files
import time

def test():

    input = [

        "123 328  51 64 ",
        " 45 64  387 23 ",
        "  6 98  215 314",        
        "*   +   *   +  ", 

    ]

    return input

def parse(input):

    math = []
    params = []

    for line in input:

        split = line.split()

        if "+" in line:
            for param in split:
                params.append(param)
    
        else:
            for index, number in enumerate(split):
                if index < len(math):
                    math[index].append(int(number))
                else:
                    math.append([int(number)])

    return math, params

def whitespace(input):

    math = []
    params = []
    separated = []
    empty = []

    for line in input:


        if "+" in line:
            for param in line.split():
                params.append(param)

        else:
            split = list(line)
            separated.append(split)

    transposed = [list(row) for row in zip(*separated)]

    for line in transposed:

        combined = "".join(line)
        combined = combined.strip()
        
        if combined == "":
            math.append(empty)
            empty = []

        else:
            empty.append(int(combined))

    math.append(empty)

    return math, params

def calculate(math, params):

    answer = 0

    for index, numbers in enumerate(math):

        param = params[index]
        temp = 0

        if param == "+":
            for number in numbers:
                temp += number

        elif param == "*":
            temp = 1
            for number in numbers:
                 temp*= number
        
        answer += temp

    return answer

def part1(input):

    math, params = parse(input)
    answer = calculate(math, params)

    print("Part 1: {}".format(answer))


def part2(input):

    math, params = whitespace(input)
    answer = calculate(math, params)

    print("Part 2: {} ".format(answer))

filename = "../input/06.txt"
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