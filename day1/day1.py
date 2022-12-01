print(sorted([sum(map(int, x.split("\n"))) for x in open("in").read().split("\n\n")[:-1]])[:-int(input())-1:-1])

### Documented version 
sorted( # sort sums because... u know
    [
        sum(map(int, x.split("\n"))) # sum inv of a single came
        for x in open("in").read().split("\n\n")[:-1] # read input and split into per-camel list
    ]
)[:-int(input())-1:-1] # reverse the sort and get the first `n` elements as per stdin input


