#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-15 22:22
FileName: P1022. 从根到叶的二进制数之和
Description:
"""
from typing import Optional

from icecream import ic

from utils.node import TreeNode


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        paths = 0

        def dfs(node, path):
            nonlocal paths
            if not node:
                return
            path = path * 2 + node.val
            if not node.left and not node.right:
                paths += path
            else:
                dfs(node.left, path)
                dfs(node.right, path)

        dfs(root, 0)
        return paths


if __name__ == '__main__':
    root = TreeNode.create('[1,0,1,0,1,0,1]')
    solution = Solution().sumRootToLeaf(root)
    ic(solution)
