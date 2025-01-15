#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-14 23:20
FileName: P0113. 路径总和 II
Description:
"""
from typing import Optional, List

from icecream import ic

from utils.node import TreeNode


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        paths = []

        def dfs(node, path):
            if not node:
                return
            path.append(node.val)
            if not node.left and not node.right:
                if targetSum == sum(path):
                    paths.append(path.copy())
            dfs(node.left, path)
            dfs(node.right, path)
            path.pop()

        dfs(root, [])

        return paths


if __name__ == '__main__':
    root = TreeNode.create('[5,4,8,11,null,13,4,7,2,null,null,5,1]')
    solution = Solution().pathSum(root, 22)
    ic(solution)
