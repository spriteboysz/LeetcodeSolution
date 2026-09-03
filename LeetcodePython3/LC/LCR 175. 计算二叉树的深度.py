#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-03 20:33
FileName: LC/LCR 175. 计算二叉树的深度.py
Description: 
"""
from typing import Optional

from utils.node import TreeNode


class Solution:
    def calculateDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.calculateDepth(root.left), self.calculateDepth(root.right)) + 1


if __name__ == '__main__':
    solution = Solution().calculateDepth(TreeNode('[1, 2, 2, 3, null, null, 5, 4, null, null, 4]'))
    print(solution)
