#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-27 22:39
FileName: algorithm/P0563. 二叉树的坡度.py
Description: 
"""
from typing import Optional

from icecream import ic

from utils.node import TreeNode


class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0, 0
            sl, pl = dfs(node.left)
            sr, pr = dfs(node.right)
            return sr + sl + node.val, abs(sl-sr) + pl + pr

        _, tilt = dfs(root)
        return tilt


if __name__ == '__main__':
    solution = Solution().findTilt(TreeNode.create('[4,2,9,3,5,null,7]'))
    ic(solution)
