#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-06 23:03
FileName: P0094. 二叉树的中序遍历.py
Description:
"""
from typing import Optional, List

from utils.node import TreeNode


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node: TreeNode | None):
            if not node:
                return
            dfs(node.left)
            values.append(node.val)
            dfs(node.right)

        values = []
        dfs(root)
        return values


if __name__ == '__main__':
    solution = Solution().inorderTraversal(TreeNode('[1,null,2,3]'))
    print(solution)
