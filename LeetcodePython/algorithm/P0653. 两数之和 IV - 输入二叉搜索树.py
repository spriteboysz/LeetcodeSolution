#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-30 22:13
FileName: P0653. 两数之和 IV - 输入二叉搜索树
Description:
"""
from typing import Optional

from utils.node import TreeNode


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def dfs(node):
            if not node:
                return
            values.append(node.val)
            dfs(node.left)
            dfs(node.right)

        values = []
        dfs(root)
        for i, num in enumerate(values[:-1]):
            if k - num in set(values[i + 1:]):
                return True
        return False


if __name__ == '__main__':
    root = TreeNode().create('[5,3,6,2,4,null,7]')
    solution = Solution().findTarget(root, 9)
    print(solution)
