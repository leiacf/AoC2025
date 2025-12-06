#Advent of Code 2025 Day 05

from tools import files
import time
import copy

def test():

    input = [

        "3-5",
        "10-14",
        "16-20",
        "12-18",
        "",
        "1",
        "5",
        "8",
        "11",
        "17",
        "32"

    ]

    return input

def parse(input):

    cut = 0
    ranges = []
    ingredients = []

    for index, entry in enumerate(input):

        if entry == "":
            cut = index
            break

    first = input[:cut]
    second = input[cut+1:]

    for entry in first:

        numbers = [int(x) for x in entry.split("-")]
        ranges.append(numbers)

    for ingredient in second:
        
        ingredients.append(int(ingredient))

    ingredients.sort()
    ranges.sort()

    return ranges, ingredients

def search(ranges, ingredients):

    fresh = 0

    for ingredient in ingredients:
        for small, large in ranges:

            if ingredient >= small and ingredient <= large:
                fresh += 1
                break

    return fresh

def combine(combined):

    out = [combined[0]]

    for inRange in combined:

        trigger = check(inRange, out)

        if not trigger:
            out.append(inRange)

    return out

def check(inRange, out):

    inMin, inMax = inRange

    for x in range(0, len(out)):

        outRange = out[x]
        outMin, outMax = outRange
            
        if (inMin <= outMin) and (outMax <= inMax):
            out[x] = inRange # in is bigger than out
            return True
        
        elif (outMin <= inMin) and (inMax <= outMax):
            return True # already in list
        
        elif (outMin <= inMin) and (inMin <= outMax) and (outMax <= inMax):
            out[x] = [outMin, inMax] # left overlap for max
            return True

    return False

def calculate(combined):

    answer = 0

    for entry in combined:
        start, stop = entry

        answer += stop-start+1

    return answer

def part1(input):

    ranges, ingredients = parse(input)
    answer = search(ranges, ingredients)
    
    print("Part 1: {}".format(answer))


def part2(input):

    ranges, _ = parse(input)
    combined = combine(ranges)
    answer = calculate(combined)

    print("Part 2: {} ".format(answer))

filename = "../input/05.txt"
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