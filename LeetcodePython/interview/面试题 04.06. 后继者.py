#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-22 22:33
FileName: 面试题 04.06. 后继者
Description:
"""
from utils.node import TreeNode


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode | None:
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
    root = TreeNode.create('[5,3,6,2,4,null,null,1]')
    p = TreeNode(5)
    solution = Solution().inorderSuccessor(root, p)
    print(solution)
