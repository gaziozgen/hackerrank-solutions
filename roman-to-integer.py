
# https://leetcode.com/problems/roman-to-integer/
# 17.10.2020


class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        s = s + "I"
        for i in range(len(s)-1):
            if s[0] == "I":
                if s[1] == "I":
                    num += 1
                else:
                    num -= 1

            if s[0] == "V":
                if s[1] in ("V", "I"):
                    num += 5
                else:
                    num -= 5

            if s[0] == "X":
                if s[1] in ("V", "I", "X"):
                    num += 10
                else:
                    num -= 10

            if s[0] == "L":
                if s[1] in ("D", "M", "C"):
                    num -= 50
                else:
                    num += 50

            if s[0] == "C":
                if s[1] in ("D", "M"):
                    num -= 100
                else:
                    num += 100

            if s[0] == "D":
                if s[1] == "M":
                    num -= 500
                else:
                    num += 500

            if s[0] == "M":
                num += 1000
            s = s[1:]
        return num
