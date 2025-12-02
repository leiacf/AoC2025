#Advent of Code 2025 Day 02

from tools import files
import time

def test():

    input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224, 1698522-1698528,446443-446449,38593856-38593862,565653-565659, 824824821-824824827,2121212118-2121212124"

    return input

def parse(input):

    data = []

    ranges = input.split(",")
    
    for numbers in ranges:
        first, last = numbers.split("-")
        first = int(first)
        last = int(last)

        data.append([first, last])

    return data

def calculate(data):

    answer = 0

    for first, last in data:
        for number in range(first, last+1):

            if hasRepeating(number):
                answer += number

    return answer

def hasRepeating(number):

    num = str(number)
    half = len(num)//2
 
    if num[0:half] == num[half:]:
        return True
    
    return False

def calculateAgain(data):

    answer = 0

    for first, last in data:
        for number in range(first, last+1):

            if hasSeveralRepeating(number):
                answer += number

    return answer

def hasSeveralRepeating(number):

    num = str(number)

    for segment in range(1, len(num)):

        if len(num) % segment == 0:
            test = num[0:segment]

            if num.count(test) == len(num) // segment:
                return True                
        
    return False


def part1(input):

    data = parse(input)

    answer = calculate(data)

    print("Part 1: The sum of all invalid IDs is {}".format(answer))


def part2(input):

    data = parse(input)

    answer = calculateAgain(data)

    print("Part 2: The sum of all invalid IDs is {} ".format(answer))

filename = "../input/02.txt"
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