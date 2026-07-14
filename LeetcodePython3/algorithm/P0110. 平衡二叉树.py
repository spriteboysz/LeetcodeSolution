#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-13 22:21
FileName: P0110. 平衡二叉树.py
Description:
"""
from typing import Optional

from utils.node import TreeNode


class Solution:
    def high(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.high(root.left), self.high(root.right))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return abs(self.high(root.left) - self.high(root.right)) <= 1 and self.isBalanced(
            root.left) and self.isBalanced(root.right)


if __name__ == '__main__':
    solution = Solution().isBalanced(TreeNode('[3,9,20,null,null,15,7]'))
    print(solution)
