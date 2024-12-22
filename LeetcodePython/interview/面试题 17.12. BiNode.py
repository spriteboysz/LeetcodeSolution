#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-22 20:12
FileName: 面试题 17.12. BiNode
Description:
"""
from typing import Optional

from utils.node import TreeNode


class Solution:
    def convertBiNode(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        dummy = TreeNode(-1)
        curr = dummy

        def dfs(node):
            if not node:
                return
            nonlocal curr
            dfs(node.left)
            node.left = None
            curr.right = node
            curr = curr.right
            dfs(node.right)

        dfs(root)
        return dummy.right


if __name__ == '__main__':
    root = TreeNode.create('[4,2,5,1,3,null,6,0]')
    solution = Solution().convertBiNode(root)
    print(solution)
