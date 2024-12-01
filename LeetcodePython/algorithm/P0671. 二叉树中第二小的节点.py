#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-30 22:20
FileName: P0671. 二叉树中第二小的节点
Description:
"""
from typing import Optional

from utils.node import TreeNode


class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        values = set()

        def dfs(node):
            if not node:
                return
            values.add(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        sort = sorted(list(values))
        if len(sort) < 2:
            return -1
        return sort[1]


if __name__ == '__main__':
    root = TreeNode().create('[2,2,5,null,null,5,7]')
    solution = Solution().findSecondMinimumValue(root)
    print(solution)
