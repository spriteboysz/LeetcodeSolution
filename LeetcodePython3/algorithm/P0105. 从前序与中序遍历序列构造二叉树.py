#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-14 23:02
FileName: P0105. 从前序与中序遍历序列构造二叉树.py
Description:
"""
from typing import List, Optional

from utils.node import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:1 + index], inorder[:index])
        root.right = self.buildTree(preorder[1 + index:], inorder[index + 1:])
        return root


if __name__ == '__main__':
    solution = Solution().buildTree(preorder=[3, 9, 20, 15, 7], inorder=[9, 3, 15, 20, 7])
    print(solution)
