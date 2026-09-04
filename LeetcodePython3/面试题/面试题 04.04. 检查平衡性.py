#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-04 11:01
FileName: 面试题/面试题 04.04. 检查平衡性.py
Description: 
"""
from functools import lru_cache
from typing import Optional

from utils.node import TreeNode


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        @lru_cache
        def high(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            return max(high(node.left), high(node.right)) + 1

        if not root:
            return True
        return abs(high(root.left) - high(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(
            root.right)


if __name__ == '__main__':
    solution = Solution().isBalanced(TreeNode('[3,9,20,null,null,15,7]'))
    print(solution)
