#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-19 22:13
FileName: P0235. 二叉搜索树的最近公共祖先.py
Description:
"""
from utils.node import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root


if __name__ == '__main__':
    solution = Solution().lowestCommonAncestor(
        TreeNode('[6,2,8,0,4,7,9,null,null,3,5]'),
        TreeNode(2), TreeNode(8)
    )
    print(solution)
