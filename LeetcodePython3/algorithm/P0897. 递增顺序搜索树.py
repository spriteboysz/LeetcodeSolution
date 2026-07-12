#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-12 21:25
FileName: P0897. 递增顺序搜索树.py
Description:
"""
from typing import Optional

from utils.node import TreeNode


class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nodes = []

        def dfs(node: Optional[TreeNode]):
            if not node:
                return
            dfs(node.left)
            nodes.append(node)
            dfs(node.right)

        dfs(root)

        for i, node in enumerate(nodes):
            node.left = None
            node.right = None if i == len(nodes) - 1 else nodes[i + 1]
        return nodes[0]


if __name__ == '__main__':
    solution = Solution().increasingBST(TreeNode('[5,3,6,2,4,null,8,1,null,null,null,7,9]'))
    print(solution)
