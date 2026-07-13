#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-12 22:28
FileName: P0543. 二叉树的直径.py
Description:
"""
from typing import Optional

from utils.node import TreeNode


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maximum = 1

        def dfs(node: Optional[TreeNode]):
            nonlocal maximum
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            maximum = max(maximum, left + right + 1)
            return max(left, right) + 1

        dfs(root)
        return maximum - 1


if __name__ == '__main__':
    solution = Solution().diameterOfBinaryTree(TreeNode([1, 2, 3, 4, 5]))
    print(solution)
