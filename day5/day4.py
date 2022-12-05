import numpy as np


stacks = [
    [" ", " ", " ", " ", " ", "Q", " ", "P", "P"],
    [" ", " ", " ", " ", "G", "V", "S", "Z", "F"],
    [" ", " ", " ", "W", "V", "F", "Z", "W", "Q"],
    [" ", " ", "V", "T", "N", "J", "W", "B", "W"],
    [" ", "Z", "L", "V", "B", "C", "R", "N", "M"],
    ["C", "W", "R", "H", "H", "P", "T", "M", "B"],
    ["Q", "Q", "M", "Z", "Z", "N", "G", "G", "J"],
    ["B", "R", "B", "C", "D", "H", "D", "C", "N"],
]

stacks: list[list] = [
    [elem for elem in stack[::-1] if elem != " " ]
    for stack in np.array(stacks).T
]

content = [
    list(map(int, [components[1], components[3], components[5]]))
    for line in open("in").readlines()[10:]
    if (components := line.strip().split())
]

for instruction in content:
    print(instruction)
    # Part 1
    # for _ in range(instruction[0]):
    #     stacks[instruction[2] - 1].append(stacks[instruction[1] - 1].pop())
    to_remove = [stacks[instruction[1] - 1].pop() for _ in range(instruction[0])]
    for elem in to_remove[::-1]:
        stacks[instruction[2] - 1].append(elem)

for stack in stacks:
    print(stack.pop())

