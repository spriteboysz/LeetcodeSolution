#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-14 23:07
FileName: P0257. 二叉树的所有路径
Description:
"""
from typing import Optional, List

from icecream import ic

from utils.node import TreeNode


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []

        def dfs(node, path):
            if not node:
                return
            path += str(node.val)
            if not node.left and not node.right:
                paths.append(path)
            else:
                path += '->'
                dfs(node.left, path)
                dfs(node.right, path)

        dfs(root, '')
        return paths


if __name__ == '__main__':
    root = TreeNode.create('[1,2,3,null,5]')
    solution = Solution().binaryTreePaths(root)
    ic(solution)
