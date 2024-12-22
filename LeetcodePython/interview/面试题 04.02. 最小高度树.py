#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-22 22:06
FileName: 面试题 04.02. 最小高度树
Description:
"""
from typing import List, Optional

from utils.node import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def create(left, right):
            if left >= right:
                return
            mid = left + (right - left) // 2
            node = TreeNode(nums[mid])
            node.left = create(left, mid)
            node.right = create(mid + 1, right)
            return node

        return create(0, len(nums))


if __name__ == '__main__':
    solution = Solution().sortedArrayToBST([-10, -3, 0, 5, 9])
    print(solution)
