#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-01 11:44
FileName: LC/LC 44. 开幕式焰火.py
Description: 
"""
from utils.node import TreeNode


class Solution:
    def numColor(self, root: TreeNode) -> int:
        colors = set()

        def dfs(node):
            if not node:
                return
            colors.add(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return len(colors)


if __name__ == '__main__':
    solution = Solution().numColor(TreeNode('[1,3,2,1,null,2]'))
    print(solution)
