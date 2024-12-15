#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-15 10:34
FileName: LCR 175. 计算二叉树的深度
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
    root = TreeNode.create('[1, 2, 2, 3, null, null, 5, 4, null, null, 4]')
    solution = Solution().calculateDepth(root)
    print(solution)
