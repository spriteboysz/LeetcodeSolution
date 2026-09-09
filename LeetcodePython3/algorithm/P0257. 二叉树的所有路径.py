#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-08 16:43
FileName: algorithm/P0257. 二叉树的所有路径.py
Description: 
"""
from typing import Optional, List

from utils.node import TreeNode


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(node: Optional[TreeNode], path):
            if not node:
                return
            path.append(str(node.val))
            if not node.left and not node.right:
                paths.append('->'.join(path.copy()))

            dfs(node.left, path)
            dfs(node.right, path)
            path.pop()

        paths = []
        dfs(root, [])
        return paths


if __name__ == '__main__':
    solution = Solution().binaryTreePaths(TreeNode('[1,2,3,null,5]'))
    print('<None>' if not solution else f'{solution=}')
