
# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# 23.10.2020


class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
