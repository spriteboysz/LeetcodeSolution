#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-10 20:03
FileName: P0145. 二叉树的后序遍历
Description:
"""
from typing import Optional, List

from utils.node import TreeNode


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        values = []

        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            dfs(node.right)
            values.append(node.val)

        dfs(root)
        return values


if __name__ == '__main__':
    root = TreeNode.create('[1,2,3,4,5,null,8,null,null,6,7,9]')
    solution = Solution().postorderTraversal(root)
    print(solution)
