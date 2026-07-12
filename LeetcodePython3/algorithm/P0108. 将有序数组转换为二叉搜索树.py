#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-11 23:31
FileName: P0108. 将有序数组转换为二叉搜索树.py
Description:
"""
from typing import List, Optional

from utils.node import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build(data: List[int]):
            if not data:
                return None
            index = len(data) // 2
            return TreeNode(
                data[index],
                left=build(data[:index]),
                right=build(data[index + 1:])
            )

        return build(nums)


if __name__ == '__main__':
    solution = Solution().sortedArrayToBST([-10, -3, 0, 5, 9])
    print(solution)
