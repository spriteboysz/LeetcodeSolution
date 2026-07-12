#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-11 23:07
FileName: P0654. 最大二叉树.py
Description:
"""
from typing import List, Optional

from utils.node import TreeNode


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def build(data: List[int]):
            if not data:
                return None
            index = data.index(max(data))
            node = TreeNode(data[index])
            node.left = build(data[:index])
            node.right = build(data[index + 1:])
            return node

        return build(nums)


if __name__ == '__main__':
    solution = Solution().constructMaximumBinaryTree([3, 2, 1, 6, 0, 5])
    print(solution)
