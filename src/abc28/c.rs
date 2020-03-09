#[allow(dead_code)]
pub fn c(a: Vec<usize>) -> usize {
    let mut l = Vec::new();
    for x in 0..5 {
        for y in x + 1..5 {
            for z in y + 1..5 {
                let sum = a[x] + a[y] + a[z];
                if !l.contains(&sum) {
                    l.push(sum);
                }
            }
        }
    }
    l.sort();
    l.reverse();
    l[2]
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test1() {
        assert_eq!(c([1, 2, 3, 4, 5].to_vec()), 10);
    }

    #[test]
    fn test2() {
        assert_eq!(c([1, 2, 3, 5, 8].to_vec()), 14);
    }
}
