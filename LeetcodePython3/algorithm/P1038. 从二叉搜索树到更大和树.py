#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-11 22:42
FileName: P1038. 从二叉搜索树到更大和树.py
Description:
"""
from typing import Optional

from utils.node import TreeNode


class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node: Optional[TreeNode]):
            nonlocal acc
            if not node:
                return
            dfs(node.right)
            acc += node.val
            node.val = acc
            dfs(node.left)

        acc = 0
        dfs(root)
        return root


if __name__ == '__main__':
    solution = Solution().bstToGst(TreeNode('[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]'))
    print(solution)
