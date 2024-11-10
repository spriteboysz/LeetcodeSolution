#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-10 23:28
FileName: P0104. 二叉树的最大深度
Description:
"""
from typing import Optional

from utils.node import TreeNode


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


if __name__ == '__main__':
    root = TreeNode.create('[3,9,20,null,null,15,7]')
    solution = Solution().maxDepth(root)
    print(solution)
