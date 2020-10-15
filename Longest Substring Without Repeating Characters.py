
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# 14.10.2020


class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = [""]
        counter = 0
        for i in range(len(s)):
            if not s[i] in sub[counter]:
                sub[counter] += s[i]
            else:
                for j in range(len(sub[counter])):
                    if s[i] == sub[counter][j]:
                        sub.append(s[i+j-len(sub[counter])+1:i+1])
                        sub[counter] = len(sub[counter])
                        counter += 1
                        break

        sub[counter] = len(sub[counter])
        return max(sub)
