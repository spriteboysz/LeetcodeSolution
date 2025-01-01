#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-01 18:50
FileName: LCR 054. 把二叉搜索树转换为累加树
Description:
"""
from utils.node import TreeNode


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        acc = 0

        def dfs(node):
            if not node:
                return
            nonlocal acc
            dfs(node.right)
            acc += node.val
            node.val = acc
            dfs(node.left)

        dfs(root)
        return root


if __name__ == '__main__':
    root = TreeNode.create('[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]')
    solution = Solution().convertBST(root)
    print(solution)
