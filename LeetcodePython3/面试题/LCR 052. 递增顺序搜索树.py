#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-05 18:20
FileName: 面试题/LCR 052. 递增顺序搜索树.py
Description: 
"""
from utils.node import TreeNode


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def dfs(node: TreeNode):
            if not node:
                return
            dfs(node.left)
            nodes.append(node)
            dfs(node.right)

        if not root:
            return root

        nodes = []
        dfs(root)

        for i, n in enumerate(nodes):
            n.left = None
            n.right = None if i == len(nodes) - 1 else nodes[i + 1]
        return nodes[0]


if __name__ == '__main__':
    solution = Solution().increasingBST(TreeNode('[5,3,6,2,4,null,8,1,null,null,null,7,9]'))
    print(solution)
