#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-12 22:52
FileName: P0235. 二叉搜索树的最近公共祖先
Description:
"""

from utils.node import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == p or root == q:
            return root
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root


if __name__ == '__main__':
    root = TreeNode.create('[6,2,8,0,4,7,9,null,null,3,5]')
    p = TreeNode.create('[2]')
    q = TreeNode.create('[8]')
    solution = Solution().lowestCommonAncestor(root, p, q)
    print(solution)
