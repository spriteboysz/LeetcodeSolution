#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-01 21:37
FileName: LCR/LCR 144. 翻转二叉树.py
Description: 
"""
from typing import Optional

from utils.node import TreeNode


class Solution:
    def flipTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        root.right, root.left = self.flipTree(root.left), self.flipTree(root.right)
        return root


if __name__ == '__main__':
    solution = Solution().flipTree(TreeNode([5, 7, 9, 8, 3, 2, 4]))
    print(solution)
