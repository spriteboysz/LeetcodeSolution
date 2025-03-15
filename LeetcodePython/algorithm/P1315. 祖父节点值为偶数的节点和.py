#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-15 19:10
FileName: algorithm/P1315. 祖父节点值为偶数的节点和.py
Description: 
"""
from typing import Optional

from icecream import ic

from utils.node import TreeNode


class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            nonlocal ss
            if node.val % 2 == 0:
                if node.left:
                    if node.left.left:
                        ss += node.left.left.val
                    if node.left.right:
                        ss += node.left.right.val
                if node.right:
                    if node.right.left:
                        ss += node.right.left.val
                    if node.right.right:
                        ss += node.right.right.val
            dfs(node.left)
            dfs(node.right)

        ss = 0
        dfs(root)
        return ss


if __name__ == '__main__':
    tree = TreeNode.create('[6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]')
    solution = Solution().sumEvenGrandparent(tree)
    ic(solution)
