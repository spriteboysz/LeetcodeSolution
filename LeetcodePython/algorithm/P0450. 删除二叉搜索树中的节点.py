#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-06 22:41
FileName: P0450. 删除二叉搜索树中的节点
Description:
"""
from typing import Optional

from utils.node import TreeNode


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        values = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            values.append(node.val)
            dfs(node.right)

        dfs(root)
        values = [value for value in values if value != key]

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
    root = TreeNode.create('[5,3,6,2,4,null,7]')
    solution = Solution().deleteNode(root, 3)
    print(solution)
