class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()

        sign = ""
        if len(s) > 0 and s[0] in ["+", "-"]:
            sign = s[0]
            s = s[1:]
        for i in range(len(s)):
            if not s[i].isdigit():
                s = s[:i]
                break

        if s == "":
            return 0

        s_int = int(sign + s)
        if s_int < -(2 ** 31):
            s_int = -(2 ** 31)
        if s_int > 2 ** 31 - 1:
            s_int = 2 ** 31 - 1
        return s_int
