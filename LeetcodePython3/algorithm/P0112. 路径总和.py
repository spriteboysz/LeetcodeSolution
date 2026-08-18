#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-17 23:14
FileName: algorithm/P0112. 路径总和.py
Description: 
"""
from typing import Optional

from utils.node import TreeNode


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node: Optional[TreeNode], x: int):
            if not node:
                return False
            x += node.val
            if not node.left and not node.right:
                return x == targetSum
            left = dfs(node.left, x)
            right = dfs(node.right, x)
            return left or right

        return dfs(root, 0)


if __name__ == '__main__':
    solution = Solution().hasPathSum(
        TreeNode('[5,4,8,11,null,13,4,7,2,null,null,null,1]'),
        targetSum=23
    )
    print(solution)
