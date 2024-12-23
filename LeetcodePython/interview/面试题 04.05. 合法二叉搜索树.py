#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-22 22:23
FileName: 面试题 04.05. 合法二叉搜索树
Description:
"""
from typing import Optional

from utils.node import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        value = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            value.append(node.val)
            dfs(node.right)

        dfs(root)
        return len(value) == len(set(value)) and value == sorted(value)


if __name__ == '__main__':
    root = TreeNode.create('[2,1,3]')
    solution = Solution().isValidBST(root)
    print(solution)
