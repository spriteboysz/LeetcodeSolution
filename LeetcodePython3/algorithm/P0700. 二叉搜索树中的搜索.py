#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-12 09:53
FileName: P0700. 二叉搜索树中的搜索.py
Description:
"""
from typing import Optional

from utils.node import TreeNode


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val > val:
            return self.searchBST(root.left, val)
        if root.val < val:
            return self.searchBST(root.right, val)
        return root


if __name__ == '__main__':
    solution = Solution().searchBST(TreeNode([4, 2, 7, 1, 3]), 2)
    print(solution)
