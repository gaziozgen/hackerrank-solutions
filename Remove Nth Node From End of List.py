
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# 15.10.2020


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        temp, prev, counter = head, None, 0

        if not head.next:
            return None

        while temp:
            temp = temp.next
            counter += 1
        temp = head

        for i in range(counter - n):
            prev = temp
            temp = temp.next

        while temp.next:
            temp.val = temp.next.val
            prev = temp
            temp = temp.next

        prev.next = None

        return head
