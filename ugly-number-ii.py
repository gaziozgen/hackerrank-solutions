
# https://leetcode.com/problems/ugly-number-ii/
# 16.10.2020

uglies = [1]
for i in range(31):
    for j in range(20):
        for k in range(14):
            uglies.append(2**i*3**j*5**k)
uglies.sort()


class Solution:
    def nthUglyNumber(self, n: int) -> int:

        return uglies[n]
