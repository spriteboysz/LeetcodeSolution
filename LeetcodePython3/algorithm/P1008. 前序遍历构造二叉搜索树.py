#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-14 23:18
FileName: P1008. 前序遍历构造二叉搜索树.py
Description:
"""
from typing import Optional, List

from utils.node import TreeNode


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        for i, num in enumerate(preorder):
            if num > preorder[0]:
                index = i
                break
        else:
            index = len(preorder)
        root = TreeNode(preorder[0])
        root.left = self.bstFromPreorder(preorder[1:index])
        root.right = self.bstFromPreorder(preorder[index:])
        return root


if __name__ == '__main__':
    solution = Solution().bstFromPreorder(preorder=[8, 5, 1, 7, 10, 12])
    print(solution)
