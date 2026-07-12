#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-12 09:33
FileName: P0617. 合并二叉树.py
Description:
"""
from typing import Optional

from utils.node import TreeNode


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node1: Optional[TreeNode], node2: Optional[TreeNode]):
            if not node1 and not node2:
                return None
            if not node1:
                return node2
            if not node2:
                return node1
            left = dfs(node1.left, node2.left)
            node = TreeNode(node1.val + node2.val)
            right = dfs(node1.right, node2.right)
            node.left = left
            node.right = right
            return node

        return dfs(root1, root2)


if __name__ == '__main__':
    solution = Solution().mergeTrees(TreeNode([1, 3, 2, 5]), TreeNode(['[2,1,3,null,4,null,7]']))
    print(solution)
