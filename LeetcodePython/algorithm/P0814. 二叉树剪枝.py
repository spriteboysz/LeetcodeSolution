#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-15 22:13
FileName: P0814. 二叉树剪枝
Description:
"""
from typing import Optional

from icecream import ic

from utils.node import TreeNode


class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        left, right = self.pruneTree(root.left), self.pruneTree(root.right)
        if not root.val and not left and not right:
            return None
        return TreeNode(root.val, left, right)


if __name__ == '__main__':
    root = TreeNode.create('[1,0,1,0,0,0,1]')
    solution = Solution().pruneTree(root)
    ic(solution.__str__())
