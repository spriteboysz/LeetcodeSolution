#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-19 22:19
FileName: P0236. 二叉树的最近公共祖先.py
Description:
"""
from typing import Optional

from utils.node import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> Optional[TreeNode]:
        if root is None or root.val in [p.val, q.val]:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left or right


if __name__ == '__main__':
    solution = Solution().lowestCommonAncestor(
        TreeNode('[6,2,8,0,4,7,9,null,null,3,5]'),
        TreeNode(2), TreeNode(8)
    )
    print(solution)
