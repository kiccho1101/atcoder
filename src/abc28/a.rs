#[allow(dead_code)]
pub fn a(n: u32) -> String {
    if n <= 59 {
        String::from("Bad")
    } else if n <= 89 {
        String::from("Good")
    } else if n <= 99 {
        String::from("Great")
    } else {
        String::from("Perfect")
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test1() {
        assert_eq!(a(80), "Good");
    }

    #[test]
    fn test2() {
        assert_eq!(a(100), "Perfect");
    }

    #[test]
    fn test3() {
        assert_eq!(a(59), "Bad");
    }

    #[test]
    fn test4() {
        assert_eq!(a(95), "Great");
    }
}
