#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-29 14:06
FileName: LCR 144. 翻转二叉树
Description:
"""
from typing import Optional

from utils.node import TreeNode


class Solution:
    def flipTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        tmp = root.left
        root.left = self.flipTree(root.right)
        root.right = self.flipTree(tmp)
        return root


if __name__ == '__main__':
    root = TreeNode.create('[5,7,9,8,3,2,4]')
    solution = Solution().flipTree(root)
    print(solution)
