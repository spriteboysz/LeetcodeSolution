#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-22 22:16
FileName: 面试题 04.04. 检查平衡性
Description:
"""
from typing import Optional

from utils.node import TreeNode


class Solution:
    @classmethod
    def high(cls, root) -> int:
        if not root:
            return 0
        return max(cls.high(root.left), cls.high(root.right)) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if abs(self.high(root.left) - self.high(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)


if __name__ == '__main__':
    root = TreeNode.create('[3,9,20,null,null,15,7]')
    solution = Solution().isBalanced(root)
    print(solution)
