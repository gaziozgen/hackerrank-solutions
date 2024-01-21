
# https://leetcode.com/problems/reverse-string/
# 22.10.2020


class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(int(len(s)/2)):
            a = s[i]
            s[i] = s[-i-1]
            s[-i-1]= a
