class Solution(object):
    def isMatch(self, text, pattern):
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], "."}

        if len(pattern) >= 2 and pattern[1] == "*":
            return (
                self.isMatch(text, pattern[2:])
                or first_match
                and self.isMatch(text[1:], pattern)
            )
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])


for case in [
    ["aa", "a", False],
    ["aa", "a*", True],
    ["ab", ".*", True],
    ["aaaab", "a*b", True],
    ["aab", "c*a*b", True],
]:
    ans = Solution().isMatch(case[0], case[1])
    print(case[0], case[1], ans, case[2])
    print(ans == case[2])
