#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-12 09:40
FileName: P0226. 翻转二叉树.py
Description:
"""
from typing import Optional

from utils.node import TreeNode


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node: Optional[TreeNode]):
            if not node:
                return None
            left = dfs(node.left)
            right = dfs(node.right)
            node.left, node.right = right, left
            return node

        return dfs(root)


if __name__ == '__main__':
    solution = Solution().invertTree(TreeNode([4, 2, 7, 1, 3, 6, 9]))
    print(solution)
