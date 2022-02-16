class Solution:
    def reverse(self, x: int) -> int:
        sign = ""
        s_x = str(x)
        if x < 0:
            sign = "-"
            s_x = s_x[1:]

        unsigned = int(s_x[::-1])
        if unsigned > 2 ** 31:
            return 0

        ans = int(sign + str(unsigned))
        return ans


for case in [[123, 321], [-123, -321], [120, 21], [1534236469, 0]]:
    ans = Solution().reverse(case[0])
    print(case[0], ans, case[1])
    print(ans == case[1])
    print()
