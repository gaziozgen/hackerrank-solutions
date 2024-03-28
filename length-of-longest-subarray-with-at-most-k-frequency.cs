
# https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/
# 29.03.2024

public class Solution
{
    public int MaxSubarrayLength(int[] nums, int k)
    {
        int firstIndex = 0;
        int lastIndex = 0;
        int maxLength = 0;

        Dictionary<int, int> frequencies = new();
        while (lastIndex < nums.Length)
        {
            if (frequencies.ContainsKey(nums[lastIndex]))
            {
                if (frequencies[nums[lastIndex]] < k) 
                    frequencies[nums[lastIndex]]++;
                else
                {
                    while (nums[firstIndex] != nums[lastIndex])
                    {
                        frequencies[nums[firstIndex]] -= 1;
                        firstIndex++;
                    }
                    firstIndex++;
                }
            }
            else frequencies.Add(nums[lastIndex], 1);

            int currentLength = 1 + lastIndex - firstIndex;
            if (currentLength > maxLength) maxLength = currentLength;
            lastIndex++;
        }
        return maxLength;
    }
}
