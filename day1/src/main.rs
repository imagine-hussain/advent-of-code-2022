use std::env;
use std::fs;

fn main() {
    let args: Vec<String> = env::args().collect();
    let mut counts = fs::read_to_string(args.get(1).expect("No filename provided"))
        .expect("Can't read file")
        .split("\n\n")
        .map(|inventory| {
            inventory
                .split('\n')
                .map(|x| x.parse::<i32>().ok())
                .fold(0, |acc, x| acc + x.unwrap_or(0))
        })
        .collect::<Vec<i32>>();

    counts.sort();
    counts.reverse();

    let top_3: i32 = counts.iter().take(3).sum();
    println!("Top 3: {top_3}");
}
