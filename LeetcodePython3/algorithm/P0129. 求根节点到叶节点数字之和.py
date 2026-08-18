#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-17 23:10
FileName: algorithm/P0129. 求根节点到叶节点数字之和.py
Description: 
"""
from typing import Optional

from utils.node import TreeNode


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node: Optional[TreeNode], x: int):
            if not node:
                return
            nonlocal ans
            x = x * 10 + node.val
            if not node.left and not node.right:
                ans += x
            dfs(node.left, x)
            dfs(node.right, x)

        dfs(root, 0)
        return ans


if __name__ == '__main__':
    solution = Solution().sumNumbers(TreeNode([1, 2, 3]))
    print(solution)
