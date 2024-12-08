#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-08 21:41
FileName: P1038. 从二叉搜索树到更大和树
Description:
"""
from typing import Optional

from utils.node import TreeNode


class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        acc = 0

        def dfs(node):
            if not node:
                return
            dfs(node.right)
            nonlocal acc
            acc += node.val
            node.val = acc
            dfs(node.left)

        dfs(root)
        return root


if __name__ == '__main__':
    root = TreeNode.create('[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]')
    solution = Solution().bstToGst(root)
    print(solution)
