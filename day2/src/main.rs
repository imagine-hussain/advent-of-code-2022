fn main() {
    let content = include_str!("../in.txt").lines().into_iter().map(|line| {
        println!("{}", line);
        (
            line.chars().next().unwrap() as u8 - b'A',
            line.chars().nth(2).unwrap() as u8 - b'X',
        )
    });

    // Part 1
    let thing = content.clone().map(matchup);
    println!("Part 1: {}", thing.sum::<u32>());
    let thing2 = content.map(matchup2);
    println!("Part 2: {}", thing2.sum::<u32>());
}

fn matchup2((opp, need): (u8, u8)) -> u32 {
    let res = match need {
        0 => {
            (match opp {
                0 => 2,
                1 => 3,
                2 => 1,
                _ => unreachable!(),
            }) + 6
        }
        1 => {
            // going to draw
            opp + 1 + 3
        }
        2 => match opp {
            0 => 3,
            1 => 1,
            2 => 2,
            _ => unreachable!("invalid opponent"),
        },
        _ => unreachable!("invalid need"),
    };

    res as u32
}

// 1 3
// 2 2
// 3 1

fn matchup((opp, you): (u8, u8)) -> u32 {
    let from_win = if (opp + 1) % 3 == you {
        6 // win
    } else if you == opp {
        3 // tie
    } else {
        0 // lose
    };

    (from_win + you + 1) as u32
}
