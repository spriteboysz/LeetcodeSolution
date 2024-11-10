#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-10 20:00
FileName: P0144. 二叉树的前序遍历
Description:
"""
from typing import Optional, List

from utils.node import TreeNode


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node):
            if node is None:
                return
            values.append(node.val)
            dfs(node.left)
            dfs(node.right)

        values = []
        dfs(root)
        return values


if __name__ == '__main__':
    root = TreeNode.create('[1,2,3,4,5,null,8,null,null,6,7,9]')
    solution = Solution().preorderTraversal(root)
    print(solution)
