#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-15 21:34
FileName: algorithm/P0129. 求根节点到叶节点数字之和.py
Description: 
"""
from typing import Optional

from icecream import ic

from utils.node import TreeNode


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, val):
            if not node:
                return 0
            val = val * 10 + node.val
            if node.left is None and node.right is None:
                return val
            return dfs(node.left, val) + dfs(node.right, val)

        return dfs(root, 0)


if __name__ == '__main__':
    solution = Solution().sumNumbers(TreeNode.create('[4, 9, 0, 5, 1]'))
    ic(solution)
