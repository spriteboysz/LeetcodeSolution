#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-12 21:48
FileName: P0965. 单值二叉树.py
Description:
"""
from typing import Optional

from utils.node import TreeNode


class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                return
            dfs(node.left)
            values.add(node.val)
            dfs(node.right)

        values = set()
        dfs(root)
        return len(values) == 1


if __name__ == '__main__':
    solution = Solution().isUnivalTree(TreeNode('[1,1,1,1,1,null,1]'))
    print(solution)
