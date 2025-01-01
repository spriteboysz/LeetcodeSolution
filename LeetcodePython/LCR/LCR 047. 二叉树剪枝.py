#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-29 18:35
FileName: LCR 047. 二叉树剪枝
Description:
"""
from utils.node import TreeNode


class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode | None:
        if not root:
            return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if root.left is None and root.right is None and root.val == 0:
            return None
        return root


if __name__ == '__main__':
    root = TreeNode.create('[1,0,1,0,0,0,1]')
    solution = Solution().pruneTree(root)
    print(solution)
