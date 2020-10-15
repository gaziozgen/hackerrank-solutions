
# https://leetcode.com/problems/container-with-most-water/
# 15.10.2020


class Solution:

    def maxArea(self, height: List[int]) -> int:

        max, p1, p2 = 0, 0, len(height)-1

        while p1 < p2:
            w = (p2 - p1)*min(height[p1], height[p2])
            if w > max:
                max = w

            if height[p1] < height[p2]:
                p1 += 1
            else:
                p2 -= 1

        return max
