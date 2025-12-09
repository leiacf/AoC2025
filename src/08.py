#Advent of Code 2025 Day 08

from tools import files
import time
import math
import itertools

def test():

    input = [

        "162,817,812",
        "57,618,57",       
        "906,360,560",
        "592,479,940",
        "352,342,300",
        "466,668,158",
        "542,29,236",        
        "431,825,988",
        "739,650,466",
        "52,470,668",        
        "216,146,977",
        "819,987,18",        
        "117,168,530",
        "805,96,715",        
        "346,949,466",
        "970,615,88",        
        "941,993,340",
        "862,61,35",       
        "984,92,344",
        "425,690,689",

    ]

    return input

def parse(input):

    data = []

    for line in input:
        xyz = [int(num) for num in line.split(",")]
        data.append(xyz)

    return data

def getDistances(data):

    distances = []

    pairs = list(itertools.combinations(data, 2))

    for p, q in pairs:
        distances.append([euclid(p, q), p, q])

    distances.sort()

    return distances

def euclid(p, q):

    dist = math.sqrt( (p[0] - q[0])**2 + (p[1] - q[1])**2 + (p[2] - q[2])**2 )

    return dist

def connect(distances, data, part):

    connections = []

    for point in data:
        connections.append([point])

    for _, p, q in distances:
        
        for index, connection in enumerate(connections):

            if p in connection:
                if q in connection:
                    break

                connection.append(q)
                connections[index] = connection

                for i in range(index+1, len(connections)):
                    if q in connections[i]:

                        for point in connections[i]:

                            if point not in connection:
                                connection.append(point)
                            
                        connections[index] = connection
                        connections.remove(connections[i])
                        
                        break

                if [q] in connections:
                    connections.remove([q])

            elif q in connection:
                if p in connection:
                    break

                connection.append(p)
                connections[index] = connection

                for i in range(index+1, len(connections)):
                    if p in connections[i]:
                        for point in connections[i]:

                            if point not in connection:
                                connection.append(point)
                            
                        connections[index] = connection
                        connections.remove(connections[i])
                        break

                if [p] in connections:
                    connections.remove([p])

            if (part==2):
                if len(connections) == 1:
                    return [p, q]
    
    connections.sort(key=len, reverse=True)

    return connections

def part1(input):

    data = parse(input)

    distances = getDistances(data)

    connections = connect(distances[:1000], data, 1)

    answer = 1

    for x in range(3):
        answer *= len(connections[x])

    print("Part 1: {}".format(answer))


def part2(input):

    data = parse(input)

    distances = getDistances(data)

    points = connect(distances, data, 2)

    answer = points[0][0] * points[1][0]

    print("Part 2: {} ".format(answer))

filename = "../input/08.txt"
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