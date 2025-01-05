#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-05 22:02
FileName: P1382. 将二叉搜索树变平衡
Description:
"""
from typing import Optional

from icecream import ic

from utils.node import TreeNode


class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        values = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            values.append(node.val)
            dfs(node.right)

        dfs(root)

        def create(left, right):
            if left >= right:
                return
            mid = left + (right - left) // 2
            node = TreeNode(values[mid])
            node.left = create(left, mid)
            node.right = create(mid + 1, right)
            return node

        return create(0, len(values))


if __name__ == '__main__':
    root = TreeNode.create('[1,null,2,null,3,null,4,null,null]')
    solution = Solution().balanceBST(root)
    ic(solution.__str__())
