#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-04 09:52
FileName: LC/LCR 174. 寻找二叉搜索树中的目标节点.py
Description: 
"""
from typing import Optional

from utils.node import TreeNode


class Solution:
    def findTargetNode(self, root: Optional[TreeNode], cnt: int) -> int:
        def dfs(node):
            if not node:
                return
            dfs(node.right)
            values.append(node.val)
            dfs(node.left)

        values = []
        dfs(root)
        return values[cnt - 1]


if __name__ == '__main__':
    solution = Solution().findTargetNode(TreeNode('[7, 3, 9, 1, 5]'), 2)
    print(solution)
