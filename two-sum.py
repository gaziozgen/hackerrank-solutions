
# https://leetcode.com/problems/two-sum/
# 18.10.2020

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            if ((target-nums[i]) in nums[i+1:]):
                return [i, i+1+nums[i+1:].index(target-nums[i])]
