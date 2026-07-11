#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-11 10:59
FileName: P1305. 两棵二叉搜索树中的所有元素.py
Description:
"""
from typing import Optional, List

from utils.node import TreeNode


class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        def dfs(node: Optional[TreeNode]):
            if not node:
                return
            dfs(node.left)
            values.append(node.val)
            dfs(node.right)

        values = []
        dfs(root1)
        dfs(root2)
        return sorted(values)


if __name__ == '__main__':
    solution = Solution().getAllElements(TreeNode([2, 4, 1]), TreeNode([1, 0, 3]))
    print(solution)
