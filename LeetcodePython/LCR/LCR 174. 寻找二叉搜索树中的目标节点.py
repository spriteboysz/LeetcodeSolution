#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-14 13:30
FileName: LCR 174. 寻找二叉搜索树中的目标节点
Description:
"""
from typing import Optional

from utils.node import TreeNode


class Solution:
    def findTargetNode(self, root: Optional[TreeNode], cnt: int) -> int:
        values = []

        def dfs(node):
            if not node:
                return

            dfs(node.right)
            values.append(node.val)
            dfs(node.left)

        dfs(root)
        return values[cnt - 1]


if __name__ == '__main__':
    root = TreeNode.create('[10, 5, 15, 2, 7, null, 20, 1, null, 6, 8]')
    solution = Solution().findTargetNode(root, 4)
    print(solution)
