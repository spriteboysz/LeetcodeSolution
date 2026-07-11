#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-10 22:52
FileName: P0230. 二叉搜索树中第 K 小的元素.py
Description:
"""
from typing import Optional

from utils.node import TreeNode


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node: Optional[TreeNode]):
            if not node:
                return
            yield from dfs(node.left)
            yield node.val
            yield from dfs(node.right)

        gen = dfs(root)
        for _ in range(k - 1):
            next(gen)
        return next(gen)


if __name__ == '__main__':
    solution = Solution().kthSmallest(TreeNode('[5,3,6,2,4,null,null,1]'), 3)
    print(solution)
