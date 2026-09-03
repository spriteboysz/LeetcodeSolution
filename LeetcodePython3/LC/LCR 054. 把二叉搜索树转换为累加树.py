#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-03 08:58
FileName: LC/LCR 054. 把二叉搜索树转换为累加树.py
Description: 
"""
from utils.node import TreeNode


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        acc = 0

        def dfs(node: TreeNode) -> None:
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
    solution = Solution().convertBST(TreeNode('[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]'))
    print(solution)
