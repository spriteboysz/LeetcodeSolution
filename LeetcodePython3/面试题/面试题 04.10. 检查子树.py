#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-08 08:39
FileName: 面试题/面试题 04.10. 检查子树.py
Description: 
"""
from typing import Optional

from utils.node import TreeNode


class Solution:
    def checkSubTree(self, t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
        def check(node1, node2):
            if node1 is None or node2 is None:
                return node1 is node2
            return node1.val == node2.val and check(node1.left, node2.left) and check(node1.right, node2.right)

        if t1 is None:
            return False
        return check(t1, t2) or self.checkSubTree(t1.left, t2) or self.checkSubTree(t1.right, t2)


if __name__ == '__main__':
    solution = Solution().checkSubTree(
        t1=TreeNode([1, 2, 3]), t2=TreeNode([2])
    )
    print('<None>' if not solution else f'{solution=}')
