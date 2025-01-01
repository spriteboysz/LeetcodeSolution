#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-29 19:00
FileName: LCR 053. 二叉搜索树中的中序后继
Description:
"""
from utils.node import TreeNode


class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode'):
        nodes = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            nodes.append(node)
            dfs(node.right)

        dfs(root)
        for i, node in enumerate(nodes[:-1]):
            if node.val == p.val:
                return nodes[i + 1]
        return None


if __name__ == '__main__':
    root = TreeNode.create('[2,1,3]')
    p = TreeNode.create('[1]')
    solution = Solution().inorderSuccessor(root, p)
    print(solution)
