#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-29 23:17
FileName: P0404. 左叶子之和
Description:
"""
from typing import Optional

from utils.node import TreeNode


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ss = 0

        def dfs(root):
            nonlocal ss
            if not root:
                return 0
            if root.left and not root.left.left and not root.left.right:
                ss += root.left.val
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return ss


if __name__ == '__main__':
    root = TreeNode().create('[3,9,20,null,null,15,7]')
    solution = Solution().sumOfLeftLeaves(root)
    print(solution)
