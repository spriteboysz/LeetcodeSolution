#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-08 12:28
FileName: P0098. 验证二叉搜索树
Description:
"""
from typing import Optional

from utils.node import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        values = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            values.append(node.val)
            dfs(node.right)

        dfs(root)
        return values == sorted(set(values))


if __name__ == '__main__':
    root = TreeNode.create('[2,1,3]')
    solution = Solution().isValidBST(root)
    print(solution)
