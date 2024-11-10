#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-10 18:37
FileName: P0100. 相同的树
Description:
"""
from typing import Optional

from utils.node import TreeNode


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == '__main__':
    p = TreeNode.create('[1,2,3]')
    q = TreeNode.create('[1,2,3]')
    solution = Solution().isSameTree(p, q)
    print(solution)
