#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-30 21:36
FileName: P0938. 二叉搜索树的范围和
Description:
"""
from typing import Optional

from utils.node import TreeNode


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        values = []

        def dfs(node):
            if not node:
                return
            values.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return sum([num for num in values if low <= num <= high])


if __name__ == '__main__':
    root = TreeNode().create('[10,5,15,3,7,null,18]')
    solution = Solution().rangeSumBST(root, low=7, high=15)
    print(solution)
