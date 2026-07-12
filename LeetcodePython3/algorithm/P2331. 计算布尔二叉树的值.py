#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-11 23:18
FileName: P2331. 计算布尔二叉树的值.py
Description:
"""
from typing import Optional

from utils.node import TreeNode


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]):
            if node is None:
                return 0

            left = dfs(node.left)
            right= dfs(node.right)
            if node.val == 2:
                node.val = left or right
            elif node.val == 3:
                node.val = left and right
            return node.val

        return bool(dfs(root))



if __name__ == '__main__':
    solution = Solution().evaluateTree(TreeNode('[2,1,3,null,null,0,1]'))
    print(solution)
