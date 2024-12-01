#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-01 20:20
FileName: P0783. 二叉搜索树节点最小距离
Description:
"""
from typing import Optional

from utils.node import TreeNode


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        values = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            values.append(node.val)
            dfs(node.right)

        dfs(root)
        return min([values[i + 1] - values[i] for i in range(len(values) - 1)])


if __name__ == '__main__':
    root = TreeNode().create('[4,2,6,1,3]')
    solution = Solution().minDiffInBST(root)
    print(solution)
