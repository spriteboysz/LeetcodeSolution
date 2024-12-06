#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-05 22:49
FileName: P0114. 二叉树展开为链表
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

        def dfs(node):
            if not node:
                return
            nodes.append(node)
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        for i, node in enumerate(nodes[:-1]):
            node.left = None
            node.right = nodes[i + 1]
        if nodes:
            nodes[-1].left = None
            nodes[-1].right = None
        print(nodes[0])


if __name__ == '__main__':
    root = TreeNode().create('[1,2,5,3,4,null,6]')
    Solution().flatten(root)
