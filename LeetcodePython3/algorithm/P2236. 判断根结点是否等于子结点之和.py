#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-14 22:59
FileName: P2236. 判断根结点是否等于子结点之和.py
Description:
"""
from typing import Optional

from utils.node import TreeNode


class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        return root.val == root.left.val + root.right.val


if __name__ == '__main__':
    solution = Solution().checkTree(TreeNode([10, 4, 6]))
    print(solution)
