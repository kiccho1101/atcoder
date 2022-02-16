class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        ans = ""
        N = len(s)
        T = 2 * (numRows - 1)
        for i in range(numRows):
            numCols = (N - i - 1) // T + 1
            for j in range(numCols):
                idx = i + j * T
                if 0 < i < numRows - 1 and idx - 2 * i > -1:
                    ans += s[idx - 2 * i]

                ans += s[idx]

                if (
                    0 < i < numRows - 1
                    and j == numCols - 1
                    and idx + 2 * (numRows - i - 1) < N
                ):
                    ans += s[idx + 2 * (numRows - i - 1)]

        return ans


test_cases = [
    ["PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"],
    ["PAYPALISHIRING", 4, "PINALSIGYAHRPI"],
iest_cases = []
    ["ABA", 4, "AAB"],
    ["A", 1, "A"],
]
for case in test_cases:
    ans = Solution().convert(case[0], case[1])
    print(ans, case[2])
    print(ans == case[2])
