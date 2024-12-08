#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-08 11:50
FileName: P0701. 二叉搜索树中的插入操作
Description:
"""
from typing import Optional

from utils.node import TreeNode


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        values = [val]

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            values.append(node.val)
            dfs(node.right)

        dfs(root)
        values.sort()

        def create(left, right):
            if left >= right:
                return None
            mid = left + (right - left) // 2
            node = TreeNode(values[mid])
            node.left = create(left, mid)
            node.right = create(mid + 1, right)
            return node

        return create(0, len(values))


if __name__ == '__main__':
    root = TreeNode().create('[4,2,7,1,3]')
    solution = Solution().insertIntoBST(root, 5)
    print(solution)
