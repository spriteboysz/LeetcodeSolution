#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-30 21:57
FileName: P0617. 合并二叉树
Description:
"""
from typing import Optional

from utils.node import TreeNode


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None
        if not root1 or not root2:
            return root1 or root2
        node = TreeNode(root1.val + root2.val)
        node.left = self.mergeTrees(root1.left, root2.left)
        node.right = self.mergeTrees(root1.right, root2.right)
        return node


if __name__ == '__main__':
    root1 = TreeNode().create('[1,3,2,5]')
    root2 = TreeNode().create('[2,1,3,null,4,null,7]')
    solution = Solution().mergeTrees(root1, root2)
    print(solution)
