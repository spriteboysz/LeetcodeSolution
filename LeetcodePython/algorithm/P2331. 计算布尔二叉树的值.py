#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-30 21:42
FileName: P2331. 计算布尔二叉树的值
Description:
"""
from typing import Optional

from utils.node import TreeNode


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return True
            left = dfs(node.left)
            right = dfs(node.right)
            if node.val == 2:
                return left or right
            elif node.val == 3:
                return left and right
            else:
                return bool(node.val)

        return dfs(root)


if __name__ == '__main__':
    root = TreeNode().create('[2,1,3,null,null,0,1]')
    solution = Solution().evaluateTree(root)
    print(solution)
