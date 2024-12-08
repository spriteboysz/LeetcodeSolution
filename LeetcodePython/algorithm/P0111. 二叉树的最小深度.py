#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-08 22:08
FileName: P0111. 二叉树的最小深度
Description:
"""
from typing import Optional

from utils.node import TreeNode


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        if root.right is None:
            return self.minDepth(root.left) + 1
        if root.left is None:
            return self.minDepth(root.right) + 1

        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


if __name__ == '__main__':
    root = TreeNode.create('[3,9,20,null,null,15,7]')
    solution = Solution().minDepth(root)
    print(solution)
