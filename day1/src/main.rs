use std::env;
use std::fs;

fn main() {
    let args: Vec<String> = env::args().collect();
    let filename = args.get(1).expect("No filename provided");

    let contents = fs::read_to_string(filename).expect("Something went wrong reading the file");

    let inventory_string: Vec<&str> = contents.split("\n\n").collect();
    let mut counts: Vec<i32> = Vec::new();
    for inventory in inventory_string {
        let curr = inventory
            .split('\n')
            .map(|x| x.parse::<i32>().ok())
            .fold(0, |acc, x| acc + x.unwrap_or(0));
        // println!("{:?}", curr);
        counts.push(curr);
    }

    counts.sort();
    counts.reverse();
    let top_3: i32 = counts.iter().take(3).map(|x| {
        println!("{}", x);
        x
    }).sum();
    println!("Top 3: {top_3}");
}
