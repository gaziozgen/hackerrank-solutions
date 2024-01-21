// https://leetcode.com/problems/merge-sorted-array/
// 21.1.2024

public class Solution
{
    public void Merge(int[] nums1, int m, int[] nums2, int n)
    {
        m--;
        n--;

        for (int i = m + n + 1; i >= 0; i--)
        {
            if (n < 0 || (m > -1 && nums1[m] > nums2[n]))
                nums1[i] = nums1[m--];
            else
                nums1[i] = nums2[n--];
        }
    }
}