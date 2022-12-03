
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


def matchup(opp, you):
    """
    Game of rock paper scissors
    Returns number of points gained or lost
    1 point for rock, 2 for paper, 3 for scissors
    """
    ops_score = ord('A') - ord(opp) + 1
    your_score = ord('X') - ord(you) + 1

    if ops_score == your_score:
        return 3 + your_score

    if ops_score == 1:
        if your_score == 2:
            return 1
        else:
            return -1


