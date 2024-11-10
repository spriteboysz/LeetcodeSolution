#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-10 18:30
FileName: P0094. 二叉树的中序遍历
Description:
"""
from typing import Optional, List

from utils.node import TreeNode


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        values = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            values.append(node.val)
            dfs(node.right)

        dfs(root)
        return values


if __name__ == '__main__':
    root = TreeNode.create('[1,null,2,3]')
    solution = Solution().inorderTraversal(root)
    print(solution)
