
# https://leetcode.com/problems/single-number/
# 19.10.2020

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if not ((nums[i] in nums[i+1:]) or (nums[i] in nums[:i])):
                return nums[i]
