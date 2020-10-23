
# https://leetcode.com/problems/reverse-linked-list/
# 24.10.2020


class Solution(object):
    def reverseList(self, head):

        if head == None:
            return head

        temp = head
        arr = []
        while temp.next:
            arr.append(temp.val)
            temp = temp.next
        arr.append(temp.val)

        temp = head
        temp.val = arr.pop()
        for i in range(len(arr)):
            temp = temp.next
            temp.val = arr.pop()

        return head
