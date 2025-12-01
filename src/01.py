#Advent of Code 2025 Day 01

from tools import files
import time

def test():

    input = [

        "L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"

    ]

    return input

def parse(input):

    data = []

    for instruction in input:
       
        if instruction != "":
            letter = instruction[0]
            number = instruction[1:]
            number = int(number)

            data.append([letter, number])

    return data

def calculate(data):

    answer = 0
    current = 50

    for letter, number in data:    

        match letter:

            case "R":
                current = current + number
            case "L":
                current = current - number

        current = current % 100

        if current == 0:
            answer += 1

    return answer

def calculateLaps(data):

    answer = 0
    current = 50

    for letter, number in data:    

        match letter:
            case "R":
                temp = current + number

                for y in range(current+1, temp+1):
                    if y % 100 == 0:
                        answer +=1

                current = temp % 100
                
            case "L":
                temp = current - number

                for y in range(current-1, temp-1, -1):
                    if y % 100 == 0:
                        answer += 1

                current = temp % 100        

    return answer


def part1(input):

    data = parse(input)
    answer = calculate(data)

    print("Part 1: The code is {}".format(answer))


def part2(input):

    data = parse(input)
    answer = calculateLaps(data)

    print("Part 2: The code is {} ".format(answer))

filename = "../input/01.txt"
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