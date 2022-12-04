
content = list(map(
    lambda x: [list(map(int, y.split("-"))) for y in x.strip().split(",")],
    open("in").readlines()
))

print(len(list(filter(
    lambda x: x[0][0] <= x[1][0] <= x[1][1] <= x[0][1] or x[1][0] <= x[0][0] <= x[0][1] <= x[1][1],
    content
))))

print(len(list(filter(
    lambda x: (
        (x[0][0] <= x[1][0] <= x[0][1]) or (x[0][0] <= x[1][1] <= x[0][1])
        or
        (x[1][0] <= x[0][0] <= x[1][1]) or (x[1][0] <= x[0][1] <= x[1][1])
    ),
    content
))))

