#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-12 22:54
FileName: algorithm/P1379. 找出克隆二叉树中的相同节点.py
Description: 
"""

from icecream import ic

from utils.node import TreeNode


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfs(root1: TreeNode, root2: TreeNode):
            if root1 is None:
                return root1
            if root1 == target:
                return root2
            return dfs(root1.left, root2.left) or dfs(root1.right, root2.right)

        return dfs(original, cloned)


if __name__ == '__main__':
    tree = TreeNode.create('[7,4,3,null,null,6,19]')
    solution = Solution().getTargetCopy(tree, tree, TreeNode.create('[3]'))
    ic(solution)
