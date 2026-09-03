#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-03 16:47
FileName: LC/LCR 153. 二叉树中和为目标值的路径.py
Description: 
"""
from typing import Optional, List

from utils.node import TreeNode


class Solution:
    def pathTarget(self, root: Optional[TreeNode], target: int) -> List[List[int]]:
        paths = []

        def backtrack(node: Optional[TreeNode], path: List[int]) -> None:
            if not node:
                return

            path.append(node.val)
            if node.left is None and node.right is None and sum(path) == target:
                paths.append(path.copy())

            backtrack(node.left, path)
            backtrack(node.right, path)
            path.pop()

        backtrack(root, [])
        return paths


if __name__ == '__main__':
    solution = Solution().pathTarget(
        TreeNode('[5,4,8,11,null,13,4,7,2,null,null,5,1]'), 22
    )
    print(solution)
