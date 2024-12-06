#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-06 21:19
FileName: P0230. 二叉搜索树中第 K 小的元素
Description:
"""
from typing import Optional

from utils.node import TreeNode


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            values.append(node.val)
            dfs(node.right)

        dfs(root)
        return values[k - 1]


if __name__ == '__main__':
    root = TreeNode.create('[5,3,6,2,4,null,null,1]')
    solution = Solution().kthSmallest(root, 3)
    print(solution)
