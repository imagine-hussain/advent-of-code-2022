# Good version
print(
    "Can't read input" if (
        content := list(map(
            lambda x: [list(map(int, y.split("-"))) for y in x.strip().split(",")],
            open("in").readlines()
        ))
    ) is None else
    len(list(filter(
        lambda x: x[0][0] <= x[1][0] <= x[1][1] <= x[0][1] or x[1][0] <= x[0][0] <= x[0][1] <= x[1][1],
        content
    ))),
    len(list(filter(
        lambda x: (
            (x[0][0] <= x[1][0] <= x[0][1]) or (x[0][0] <= x[1][1] <= x[0][1])
            or
            (x[1][0] <= x[0][0] <= x[1][1]) or (x[1][0] <= x[0][1] <= x[1][1])
        ),
        content
    )))
)


# Degen version
print("Bad Input" if (content:=list(map(lambda x: [list(map(int, y.split("-"))) for y in x.strip().split(",")], open("in").readlines()))) is None else len(list(filter(lambda x: x[0][0] <= x[1][0] <= x[1][1] <= x[0][1] or x[1][0] <= x[0][0] <= x[0][1] <= x[1][1], content))), len(list(filter(lambda x: ((x[0][0] <= x[1][0] <= x[0][1]) or (x[0][0] <= x[1][1] <= x[0][1]) or (x[1][0] <= x[0][0] <= x[1][1]) or (x[1][0] <= x[0][1] <= x[1][1])), content))))
