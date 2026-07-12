#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-12 10:08
FileName: P1382. 将二叉搜索树变平衡.py
Description:
"""
from typing import Optional, List

from utils.node import TreeNode


class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node: Optional[TreeNode]):
            if not node:
                return
            dfs(node.left)
            values.append(node.val)
            dfs(node.right)

        def build(data: List[int]):
            if not data:
                return None
            mid = len(data) // 2
            return TreeNode(
                val=data[mid],
                left=build(data[:mid]),
                right=build(data[mid + 1:])
            )

        values = []
        dfs(root)
        return build(values)


if __name__ == '__main__':
    solution = Solution().balanceBST(TreeNode('[1,null,2,null,3,null,4,null,null]'))
    print(solution)
