#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-14 23:09
FileName: P0106. 从中序与后序遍历序列构造二叉树.py
Description:
"""
from typing import List, Optional

from utils.node import TreeNode


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        root = TreeNode(postorder[-1])
        index = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:index], postorder[:index])
        root.right = self.buildTree(inorder[index + 1:], postorder[index:-1])
        return root


if __name__ == '__main__':
    solution = Solution().buildTree(inorder=[9, 3, 15, 20, 7], postorder=[9, 15, 7, 20, 3])
    print(solution)
