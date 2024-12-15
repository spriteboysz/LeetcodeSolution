#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-15 10:25
FileName: LCR 052. 递增顺序搜索树
Description:
"""
from utils.node import TreeNode


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        nodes = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            nodes.append(node)
            dfs(node.right)

        dfs(root)
        for i in range(len(nodes) - 1):
            nodes[i].left = None
            nodes[i].right = nodes[i + 1]
        nodes[-1].left = None
        nodes[-1].right = None
        return nodes[0]


if __name__ == '__main__':
    root = TreeNode.create('[5,3,6,2,4,null,8,1,null,null,null,7,9]')
    solution = Solution().increasingBST(root)
    print(solution)
