#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-18 23:08
FileName: P0530. 二叉搜索树的最小绝对差.py
Description:
"""
from itertools import pairwise
from typing import Optional

from utils.node import TreeNode


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        values = []

        def dfs(node: Optional[TreeNode]):
            if not node:
                return
            dfs(node.left)
            values.append(node.val)
            dfs(node.right)

        dfs(root)
        return min(v2 - v1 for v1, v2 in pairwise(values))


if __name__ == '__main__':
    solution = Solution().getMinimumDifference(TreeNode('[4,2,6,1,3]'))
    print(solution)
