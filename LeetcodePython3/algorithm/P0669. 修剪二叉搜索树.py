#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-15 21:54
FileName: P0669. 修剪二叉搜索树.py
Description:
"""
from typing import Optional

from utils.node import TreeNode


class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val < low:
            return self.trimBST(root.right, low, high)
        if root.val > high:
            return self.trimBST(root.left, low, high)
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root


if __name__ == '__main__':
    solution = Solution().trimBST(TreeNode([1, 0, 2]), 1, 2)
    print(solution)
