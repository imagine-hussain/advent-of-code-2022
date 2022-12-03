
def matchup(opps, you):

with open('in.txt') as f:
    lines = f.readlines()
    total = 0
    for line in lines:
        line = line.strip().replace(" ", "")
        print(line)
        if not line:
            break
        total += matchup(to_thing_mean(line[0]), to_thing_friend(line[1]))

    print(total)

def to_thing_mean(c: str):
    return (
        'rock' if c == 'A' else
        'paper' if c == 'B' else
        'scissors' if c == 'C' else
        'rip lol'
    )

def to_thing_friend(c: str):
    return (
        'rock' if c == 'X' else
        'paper' if c == 'A' else
        'scissors' if c == 'P' else
        'rip lol'
    )

