// https://leetcode.com/problems/ugly-number-iii/
// 01.21.2024

public class Solution
{

    int max = 2000000000;

    public int NthUglyNumber(int n, int a, int b, int c)
    {
        int l = 1, r = max, mid, order;

        while (true)
        {
            mid = l + (r - l) / 2;
            order = OrderOfUglyNumber(mid, a, b, c);

            if (order == n)
            {
                while (order == n)
                {
                    mid--;
                    order = OrderOfUglyNumber(mid, a, b, c);
                }
                return mid + 1;
            }
            else if (order > n) r = mid - 1;
            else l = mid + 1;
        }
    }

    int OrderOfUglyNumber(int number, int a, int b, int c)
    {
        return (int)(number / a + number / b + number / c
        - number / LCM(a, b) - number / LCM(a, c) - number / LCM(b, c)
        + number / LCM(a, LCM(b, c)));
    }

    long LCM(long a, long b)
    {
        return a * b / GCD(a, b);
    }

    long GCD(long a, long b)
    {
        return b == 0 ? a : GCD(b, a % b);
    }
}