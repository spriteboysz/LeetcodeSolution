#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-07 15:05
FileName: 面试题/面试题 04.05. 合法二叉搜索树.py
Description: 
"""
from typing import Optional

from utils.node import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            values.append(node.val)
            dfs(node.right)

        values = []
        dfs(root)
        return len(values) == len(set(values)) and values == sorted(values)


if __name__ == '__main__':
    solution = Solution().isValidBST(TreeNode([2, 1, 3]))
    print('<None>' if not solution else f'{solution=}')
