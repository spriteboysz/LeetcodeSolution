#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-07 15:09
FileName: 面试题/面试题 17.12. BiNode.py
Description: 
"""
from typing import Optional

from utils.node import TreeNode


class Solution:
    def convertBiNode(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            nodes.append(node)
            dfs(node.right)
        if not root:
            return root

        nodes = []
        dfs(root)
        for i, n in enumerate(nodes[:-1]):
            n.left = None
            n.right = nodes[i + 1]
        nodes[-1].left = None
        nodes[-1].right = None
        return nodes[0]


if __name__ == '__main__':
    solution = Solution().convertBiNode(TreeNode('[4,2,5,1,3,null,6,0]'))
    print('<None>' if not solution else f'{solution=}')
