use std::collections::HashSet;

fn main() {
    let content = include_str!("input.txt");
    println!("did first iter");

    // Part 1
    let thing = content
        .lines()
        .into_iter()
        .map(|line| line.split_at(line.len() / 2))
        .into_iter()
        .map(|(lhs, rhs)| {
            let lhs_set: std::collections::HashSet<_> = lhs.chars().collect();
            let rhs_set: std::collections::HashSet<_> = rhs.chars().collect();
            *lhs_set.intersection(&rhs_set).into_iter().next().unwrap()
        })
        .map(to_priority)
        .reduce(|a, b| a + b)
        .unwrap();
    println!("thing: {}", thing);

    // Part 2
    let thing2 = content
        .lines()
        .into_iter()
        .map(|l| l.to_string())
        .collect::<Vec<_>>()
        .chunks(3)
        .into_iter()
        .map(|three_strs| {
            three_strs
                .iter()
                .map(|string| string.chars().collect::<HashSet<_>>())
                .collect::<Vec<_>>()
        })
        .map(|sets| {
            **sets[0]
                .intersection(&sets[1])
                .filter(|lhs| sets[2].contains(lhs))
                .collect::<Vec<_>>().get(0).unwrap()
        })
        .map(to_priority)
        .reduce(|a, b| a + b)
        .unwrap();
    println!("thing2: {}", thing2);
}

fn to_priority(c: char) -> u32 {
    // c to a number; a-z: 1-26; A-Z: 27-52
    (if c.is_lowercase() {
        c as u8 - b'a' + 1
    } else {
        c as u8 - b'A' + 27
    }) as u32
}
