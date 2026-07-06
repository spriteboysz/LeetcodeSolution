#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-06 23:27
FileName: P0144. 二叉树的前序遍历.py
Description:
"""
from typing import Optional, List

from utils.node import TreeNode


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node: TreeNode | None):
            values = []
            if not node:
                return values
            values.append(node.val)
            values.extend(dfs(node.left))
            values.extend(dfs(node.right))
            return values

        return dfs(root)


if __name__ == '__main__':
    solution = Solution().preorderTraversal(TreeNode('[1,2,3,4,5,null,8,null,null,6,7,9]'))
    print(solution)
