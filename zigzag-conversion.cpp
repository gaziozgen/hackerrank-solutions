https://leetcode.com/problems/zigzag-conversion/
// 17.06.2024

class Solution {
public:
    string convert(string s, int numRows) {

        if (numRows == 1) return s;

        string rows[numRows];
        int targetRow, len = s.length();

        for (int i = 0; i < len; i++) {
            targetRow = i % (2 * numRows - 2);
            if (targetRow >= numRows) targetRow = 2 * (numRows - 1) - targetRow;
            rows[targetRow] += s[i];
        }

        for (int i = 1; i < numRows; i++) rows[0] += rows[i];

        return rows[0];
    }
};