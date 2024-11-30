#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-29 23:02
FileName: P0108. 将有序数组转换为二叉搜索树
Description:
"""
from typing import Optional, List

from utils.node import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def create(left, right):
            if left >= right:
                return
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = create(left, mid)
            node.right = create(mid + 1, right)
            return node

        return create(0, len(nums))


if __name__ == '__main__':
    solution = Solution().sortedArrayToBST([-10, -3, 0, 5, 9])
    print(solution)
