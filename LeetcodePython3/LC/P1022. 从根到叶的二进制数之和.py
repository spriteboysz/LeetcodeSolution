#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-03 10:00
FileName: LC/P1022. 从根到叶的二进制数之和.py
Description: 
"""
from typing import Optional

from utils.node import TreeNode


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        ss = 0

        def dfs(node: Optional[TreeNode], v: int) -> None:
            nonlocal ss
            if not node:
                return

            v = v * 2 + node.val
            if node.left is None and node.right is None:
                ss += v
            dfs(node.left, v)
            dfs(node.right, v)

        dfs(root, 0)
        return ss


if __name__ == '__main__':
    solution = Solution().sumRootToLeaf(TreeNode([1, 0, 1, 0, 1, 0, 1]))
    print(solution)
