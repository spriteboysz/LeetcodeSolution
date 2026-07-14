#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-13 23:07
FileName: P0098. 验证二叉搜索树.py
Description:
"""
from itertools import pairwise
from typing import Optional

from utils.node import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        values = []

        def dfs(node: Optional[TreeNode]):
            if not node:
                return
            dfs(node.left)
            values.append(node.val)
            dfs(node.right)

        dfs(root)
        return all(v1 < v2 for v1, v2 in pairwise(values))


if __name__ == '__main__':
    solution = Solution().isValidBST(TreeNode([2, 1, 3]))
    print(solution)
