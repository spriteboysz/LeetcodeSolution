#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-15 17:25
FileName: LCR 176. 判断是否为平衡二叉树
Description:
"""
from typing import Optional

from utils.node import TreeNode


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def high(node):
            if not node:
                return 0
            return max(high(node.left), high(node.right)) + 1

        if not root:
            return True
        if abs(high(root.left) - high(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)


if __name__ == '__main__':
    root = TreeNode.create('[3,9,20,null,null,15,7]')
    solution = Solution().isBalanced(root)
    print(solution)
