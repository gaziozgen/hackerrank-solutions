
# https://leetcode.com/problems/container-with-most-water/
# 15.10.2020


class Solution:

    def maxArea(self, height: List[int]) -> int:
        max = 0
        p2 = len(height)-1
        p1 = 0

        while p1 < p2:
            w = (p2 - p1)*min(height[p1], height[p2])
            if w > max:
                max = w
            if height[p1] < height[p2]:
                p1 += 1
            else:
                p2 -= 1

        return max
