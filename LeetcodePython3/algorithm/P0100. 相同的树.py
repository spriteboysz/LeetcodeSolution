#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-12 22:39
FileName: P0100. 相同的树.py
Description:
"""
from typing import Optional

from utils.node import TreeNode


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == '__main__':
    solution = Solution().isSameTree(TreeNode([1, 2, 3]), TreeNode([1, 2, 3]))
    print(solution)
