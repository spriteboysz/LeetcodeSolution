#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-11 11:46
FileName: P0114. 二叉树展开为链表.py
Description:
"""
from typing import Optional

from utils.node import TreeNode


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nodes = []

        def dfs(node: Optional[TreeNode]):

            if not node:
                return
            nodes.append(node)
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        for i, node in enumerate(nodes[:-1]):
            node.left = None
            node.right = nodes[i + 1]


if __name__ == '__main__':
    Solution().flatten(TreeNode([1, 2, 5, 3, 4, 'null', 6]))
