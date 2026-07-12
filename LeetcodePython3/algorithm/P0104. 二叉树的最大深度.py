#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-12 10:01
FileName: P0104. 二叉树的最大深度.py
Description:
"""
from typing import Optional

from utils.node import TreeNode


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


if __name__ == '__main__':
    solution = Solution().maxDepth(TreeNode('[3,9,20,null,null,15,7]'))
    print(solution)
