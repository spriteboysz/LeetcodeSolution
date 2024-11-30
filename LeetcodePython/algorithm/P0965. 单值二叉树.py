#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-30 21:33
FileName: P0965. 单值二叉树
Description:
"""
from typing import Optional

from utils.node import TreeNode


class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        values = set()

        def dfs(node):
            if not node:
                return
            values.add(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return len(values) == 1


if __name__ == '__main__':
    root = TreeNode.create('[1,1,1,1,1,null,1]')
    solution = Solution().isUnivalTree(root)
    print(solution)
