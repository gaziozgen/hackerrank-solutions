
# https://leetcode.com/problems/valid-parentheses/
# 18.10.2020

chars = [')', ']', '}', '(', '[', '{']
class Solution:
    def isValid(self, s: str) -> bool:

        stack = [0]
        for i in range(len(s)):
            if s[i] in ('(', '[', '{'):
                stack.append(s[i])
            else:
                for j in range(3):
                    if s[i] == chars[j]:
                        if stack[-1] == chars[j+3]:
                            stack.pop()
                        else:
                            return False
        return stack == [0]
