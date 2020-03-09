#[allow(dead_code)]
pub fn b(s: String) -> [u32; 6] {
    let mut result: [u32; 6] = [0, 0, 0, 0, 0, 0];
    for c in s.chars() {
        if c == 'A' {
            result[0] += 1;
        } else if c == 'B' {
            result[1] += 1;
        } else if c == 'C' {
            result[2] += 1;
        } else if c == 'D' {
            result[3] += 1;
        } else if c == 'E' {
            result[4] += 1;
        } else if c == 'F' {
            result[5] += 1;
        }
    }
    result
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test1() {
        assert_eq!(b(String::from("BEAF")), [1, 1, 0, 0, 1, 1]);
    }

    #[test]
    fn test2() {
        assert_eq!(b(String::from("DECADE")), [1, 0, 1, 2, 2, 0]);
    }

    #[test]
    fn test3() {
        assert_eq!(b(String::from("ABBCCCDDDDEEEEEFFFFFF")), [1, 2, 3, 4, 5, 6]);
    }
}
