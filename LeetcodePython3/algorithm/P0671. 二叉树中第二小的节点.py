#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-15 22:13
FileName: P0671. 二叉树中第二小的节点.py
Description:
"""
from typing import Optional

from utils.node import TreeNode


class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        values = set()

        def dfs(node: Optional[TreeNode]):
            if not node:
                return
            dfs(node.left)
            values.add(node.val)
            dfs(node.right)

        dfs(root)
        return -1 if len(values) < 2 else sorted(values)[1]


if __name__ == '__main__':
    solution = Solution().findSecondMinimumValue(TreeNode('[2,2,5,null,null,5,7]'))
    print(solution)
