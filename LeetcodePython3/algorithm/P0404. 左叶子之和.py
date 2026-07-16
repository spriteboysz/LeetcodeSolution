#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-15 21:59
FileName: P0404. 左叶子之和.py
Description:
"""
from typing import Optional

from utils.node import TreeNode


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ss = 0

        def dfs(node: Optional[TreeNode]):
            nonlocal ss
            if not node:
                return 0
            if node.left and not node.left.left and not node.left.right:
                ss += node.left.val
            dfs(node.left)
            dfs(node.right)
            return ss

        dfs(root)
        return ss


if __name__ == '__main__':
    solution = Solution().sumOfLeftLeaves(TreeNode('[3,9,20,null,null,15,7]'))
    print(solution)
