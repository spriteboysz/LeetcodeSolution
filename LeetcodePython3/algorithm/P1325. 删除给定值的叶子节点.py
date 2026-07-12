#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-12 21:07
FileName: P1325. 删除给定值的叶子节点.py
Description:
"""
from typing import Optional

from utils.node import TreeNode


class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(node: Optional[TreeNode]):
            if not node:
                return None
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            if not node.left and not node.right and node.val == target:
                return None
            return node

        return dfs(root)


if __name__ == '__main__':
    solution = Solution().removeLeafNodes(TreeNode([1, 1, 1]), 1)
    print(solution)
