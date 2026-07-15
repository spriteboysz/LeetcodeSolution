#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-14 23:28
FileName: P0889. 根据前序和后序遍历构造二叉树.py
Description:
"""
from typing import List, Optional

from utils.node import TreeNode


class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not postorder:
            return None
        index = postorder.index(preorder[1]) if len(preorder) >= 2 else 0
        root = TreeNode(preorder[0])
        root.left = self.constructFromPrePost(preorder[1:index + 2], postorder[:index + 1])
        root.right = self.constructFromPrePost(preorder[index + 2:], postorder[index + 1:-1])
        return root


if __name__ == '__main__':
    solution = Solution().constructFromPrePost(preorder=[1, 2, 4, 5, 3, 6, 7], postorder=[4, 5, 2, 6, 7, 3, 1])
    print(solution)
