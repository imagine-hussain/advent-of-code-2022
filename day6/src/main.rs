use std::usize;

fn main() {
    let content = include_str!("../in").trim();

    println!("{}, {}", first_key(content, 4).unwrap(), first_key(content, 14).unwrap());

}

fn first_key(content: &str, key_size: usize) -> Result<usize, ()> {
    for i in 0..content.len()-key_size {
        let mut visited = [false; 26];
        for elem in content[i..i+key_size].bytes() {
            visited[elem as usize - b'a' as usize] = true;
        }
        if visited.iter().filter(|x| **x).count() == key_size {
            return Ok(i + key_size);
        }
    }
    Err(())
}

