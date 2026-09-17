#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-16 11:00
FileName: algorithm/P0653. 两数之和 IV - 输入二叉搜索树.py
Description: 
"""
from typing import Optional

from utils.node import TreeNode


class Solution:
    def __init__(self):
        self.values = set()

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False

        if k - root.val in self.values:
            return True
        self.values.add(root.val)
        return self.findTarget(root.left, k) or self.findTarget(root.right, k)


if __name__ == '__main__':
    solution = Solution().findTarget(TreeNode('[5,3,6,2,4,null,7]'), 9)
    print('<None>' if solution is None else f'{solution=}')
