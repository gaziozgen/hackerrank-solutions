// https://leetcode.com/problems/add-two-numbers/
// 16.06.2024

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {

        ListNode* prev = nullptr, * current, * head;
        bool carry = 0;
        int sum;

        do {
            sum = carry;
            if (l1 != nullptr) {
                sum += l1->val;
                l1 = l1->next;
            }
            if (l2 != nullptr) {
                sum += l2->val;
                l2 = l2->next;
            }

            if (sum > 9) {
                carry = 1;
                sum -= 10;
            }
            else carry = 0;

            current = new ListNode(sum);
            if (prev != nullptr) prev->next = current;
            else head = current;
            prev = current;
        } 
        while (l1 != nullptr || l2 != nullptr);

        if (carry == 1) prev->next = new ListNode(1);

        return head;
    }
};