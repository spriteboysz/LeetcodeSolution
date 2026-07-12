#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-11 23:01
FileName: P0938. 二叉搜索树的范围和.py
Description:
"""
from typing import Optional

from utils.node import TreeNode


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = 0

        def dfs(node: Optional[TreeNode]):
            nonlocal ans
            if not node:
                return
            dfs(node.left)
            if low <= node.val <= high:
                ans += node.val
            dfs(node.right)

        dfs(root)
        return ans


if __name__ == '__main__':
    solution = Solution().rangeSumBST(TreeNode('[10,5,15,3,7,null,18]'), 7, 15)
    print(solution)
