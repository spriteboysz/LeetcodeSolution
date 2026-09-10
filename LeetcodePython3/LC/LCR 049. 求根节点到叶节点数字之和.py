#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-07 13:52
FileName: 面试题/LCR 049. 求根节点到叶节点数字之和.py
Description: 
"""
from utils.node import TreeNode


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(node, path):
            if not node:
                return
            path = path * 10 + node.val
            if node.left is None and node.right is None:
                paths.append(path)
                return
            dfs(node.left, path)
            dfs(node.right, path)

        paths = []
        dfs(root, 0)
        return sum(paths)


if __name__ == '__main__':
    solution = Solution().sumNumbers(TreeNode([1, 2, 3]))
    print('<None>' if not solution else f'{solution=}')
