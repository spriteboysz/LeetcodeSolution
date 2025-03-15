#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-15 10:52
FileName: LCR/LCR 049. 求根节点到叶节点数字之和.py
Description: 
"""

from icecream import ic

from utils.node import TreeNode


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:

        def dfs(node, v):
            if not node:
                return 0
            v = v * 10 + node.val
            if node.left is None and node.right is None:
                return v
            return dfs(node.left, v) + dfs(node.right, v)

        return dfs(root, 0)


if __name__ == '__main__':
    solution = Solution().sumNumbers(TreeNode.create('[4, 9, 0, 5, 1]'))
    ic(solution)
