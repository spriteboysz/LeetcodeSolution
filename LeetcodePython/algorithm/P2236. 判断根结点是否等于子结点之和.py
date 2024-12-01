#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-30 21:49
FileName: P2236. 判断根结点是否等于子结点之和
Description:
"""
from typing import Optional

from utils.node import TreeNode


class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        return root.val == root.left.val + root.right.val


if __name__ == '__main__':
    root = TreeNode().create('[10,4,6]')
    solution = Solution().checkTree(root)
    print(solution)
