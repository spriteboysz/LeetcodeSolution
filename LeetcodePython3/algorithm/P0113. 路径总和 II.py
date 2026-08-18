#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-17 23:23
FileName: algorithm/P0113. 路径总和 II.py
Description: 
"""
from typing import Optional, List

from utils.node import TreeNode


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        paths = []

        def dfs(node: Optional[TreeNode], path: List[int]):
            if not node:
                return
            path.append(node.val)
            if not node.left and not node.right:
                if sum(path) == targetSum:
                    paths.append(path.copy())
            dfs(node.left, path)
            dfs(node.right, path)
            path.pop()

        dfs(root, [])
        return paths


if __name__ == '__main__':
    solution = Solution().pathSum(
        root=TreeNode('[5,4,8,11,null,13,4,7,2,null,null,5,1]'),
        targetSum=22
    )
    print(solution)
