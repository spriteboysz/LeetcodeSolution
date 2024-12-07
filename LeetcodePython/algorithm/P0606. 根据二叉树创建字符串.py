#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-07 23:08
FileName: P0606. 根据二叉树创建字符串
Description:
"""
from typing import Optional

from utils.node import TreeNode


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root.left and not root.right:
            return str(root.val)

        def dfs(node):
            if not node:
                return ''
            ss = str(node.val)
            left = dfs(node.left)
            ss += '(' + str(left) + ')'
            if right := dfs(node.right):
                ss += '(' + str(right) + ')'
            return ss

        return dfs(root).replace('())', ')')


if __name__ == '__main__':
    root = TreeNode.create('[1,2,3,null,4]')
    solution = Solution().tree2str(root)
    print(solution)
