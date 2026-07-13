#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-12 22:14
FileName: P0872. 叶子相似的树.py
Description:
"""
from typing import Optional, List

from utils.node import TreeNode


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode], values: List[int]):
            if not node:
                return []

            dfs(node.left, values)
            dfs(node.right, values)
            if not node.left and not node.right:
                values.append(node.val)
            return values

        return dfs(root1, []) == dfs(root2, [])


if __name__ == '__main__':
    solution = Solution().leafSimilar(
        TreeNode('[3,5,1,6,2,9,8,null,null,7,4]'),
        TreeNode('[3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]')
    )
    print(solution)
