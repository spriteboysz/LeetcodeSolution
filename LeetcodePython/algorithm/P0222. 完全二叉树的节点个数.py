#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-14 23:01
FileName: P0222. 完全二叉树的节点个数
Description:
"""
from typing import Optional

from icecream import ic

from utils.node import TreeNode


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        cnt = 0

        def dfs(node):
            nonlocal cnt
            if not node:
                return
            dfs(node.left)
            cnt += 1
            dfs(node.right)

        dfs(root)
        return cnt


if __name__ == '__main__':
    root = TreeNode.create('[1,2,3,4,5,6]')
    solution = Solution().countNodes(root)
    ic(solution)
