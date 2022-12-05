import numpy as np

stacks: list[list] = [
    [elem for elem in stack[::-1] if elem != " " ]
    for stack in np.array([
        [" ", " ", " ", " ", " ", "Q", " ", "P", "P"],
        [" ", " ", " ", " ", "G", "V", "S", "Z", "F"],
        [" ", " ", " ", "W", "V", "F", "Z", "W", "Q"],
        [" ", " ", "V", "T", "N", "J", "W", "B", "W"],
        [" ", "Z", "L", "V", "B", "C", "R", "N", "M"],
        ["C", "W", "R", "H", "H", "P", "T", "M", "B"],
        ["Q", "Q", "M", "Z", "Z", "N", "G", "G", "J"],
        ["B", "R", "B", "C", "D", "H", "D", "C", "N"],
    ]).T
]

print(
    "doing part {part}" if (part := int(input("what part: ")) in [1, 2]) else exit(),
    map(
        lambda instruction: map(
            lambda elem: stacks[instruction[2] - 1].append(elem),
            popped if (
                popped := [stacks[instruction[1] - 1].pop() for _ in range(instruction[0])] is not None and part == 1
            ) else popped[::-1]
        ), [
            list(map(int, [components[1], components[3], components[5]]))
            for line in open("in").readlines()[10:]
            if (components := line.strip().split())
        ]
    ),
    "\n",
    "".join([stack.pop() for stack in stacks])
)

