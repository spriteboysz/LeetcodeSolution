#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-29 23:23
FileName: P0226. 翻转二叉树
Description:
"""
from typing import Optional

from utils.node import TreeNode


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return
            node.left, node.right = node.right, node.left
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return root


if __name__ == '__main__':
    root = TreeNode().create('[4,2,7,1,3,6,9]')
    solution = Solution().invertTree(root)
    print(solution)
