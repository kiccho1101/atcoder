class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.max_length = 0
        self.ans = ""

        for i in range(len(s)):
            self.expand(s, i, i)
            self.expand(s, i, i + 1)

        return self.ans

    def expand(self, s, l, r):
        while l > -1 and r < len(s) and s[l] == s[r]:
            length = r - l + 1
            if self.max_length < length:
                self.max_length = length
                self.ans = s[l : r + 1]
            l -= 1
            r += 1


s = "babad"
# s = "cbbd"
print(Solution().longestPalindrome(s))
