#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-07 21:49
FileName: P0538. 把二叉搜索树转换为累加树
Description:
"""
from typing import Optional

from utils.node import TreeNode


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        acc = 0
        def dfs(node):
            nonlocal acc
            if not node:
                return
            dfs(node.right)
            acc += node.val
            print(acc)
            node.val = acc
            dfs(node.left)

        dfs(root)
        return root


if __name__ == '__main__':
    root = TreeNode.create('[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]')
    solution = Solution().convertBST(root)
    print(solution)
