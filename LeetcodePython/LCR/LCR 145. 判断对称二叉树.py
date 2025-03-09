#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-09 9:40
FileName: LCR/LCR 145. 判断对称二叉树.py
Description: 
"""
from typing import Optional

from icecream import ic

from utils.node import TreeNode


class Solution:
    def checkSymmetricTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(left, right):
            if not left and not right:
                return True
            if not left or not right or left.val != right.val:
                return False
            return dfs(left.left, right.right) and dfs(left.right, right.left)

        return dfs(root.left, root.right)


if __name__ == '__main__':
    root1 = TreeNode.create('[6,7,7,8,9,9,8]')
    solution = Solution().checkSymmetricTree(root1)
    ic(solution)
