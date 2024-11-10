#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-10 18:43
FileName: P0101. 对称二叉树
Description:
"""
from typing import Optional

from utils.node import TreeNode


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(left, right):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            if left.val != right.val:
                return False
            return check(left.right, right.left) and check(left.left, right.right)

        if root is None:
            return True
        return check(root.left, root.right)


if __name__ == '__main__':
    root = TreeNode.create('[1,2,2,3,4,4,3]')
    solution = Solution().isSymmetric(root)
    print(solution)
