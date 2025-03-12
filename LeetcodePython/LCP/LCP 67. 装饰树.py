#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-12 22:48
FileName: LCP/LCP 67. 装饰树.py
Description: 
"""
from typing import Optional

from icecream import ic

from utils.node import TreeNode


class Solution:
    def expandBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root.left:
            root.left = TreeNode(-1, left=self.expandBinaryTree(root.left))
        if root.right:
            root.right = TreeNode(-1, right=self.expandBinaryTree(root.right))
        return root


if __name__ == '__main__':
    solution = Solution().expandBinaryTree(TreeNode.create('[7,5,6]'))
    ic(solution.__str__())
