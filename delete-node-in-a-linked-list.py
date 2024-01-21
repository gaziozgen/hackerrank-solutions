
# https://leetcode.com/problems/delete-node-in-a-linked-list/
# 23.10.2020


class Solution(object):
    def deleteNode(self, node):
        prev = None
        while node.next:
            node.val = node.next.val
            prev = node
            node = node.next
        prev.next = None
