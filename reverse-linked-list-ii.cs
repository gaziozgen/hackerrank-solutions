
# https://leetcode.com/problems/reverse-linked-list-ii/
# 27.03.2024

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution
{
    public ListNode ReverseBetween(ListNode head, int left, int right)
    {

        ListNode result = head;
        ListNode prev = null;
        ListNode current = head;
        ListNode next;
        ListNode beforeLeftNode;
        ListNode leftNode;
        int count = 0;

        // skip the part that will not change
        while (count < left - 1)
        {

            prev = current;
            current = current.next;
            count++;
        }

        // cache left nodes
        beforeLeftNode = prev;
        leftNode = current;

        // reverse linked until (right + 1)th node
        while (count < right)
        {
            next = current.next;
            current.next = prev;

            prev = current;
            current = next;
            count++;
        }

        // set final links
        if (left > 1) beforeLeftNode.next = prev;
        else result = prev;
        leftNode.next = current;

        return result;

    }
}

