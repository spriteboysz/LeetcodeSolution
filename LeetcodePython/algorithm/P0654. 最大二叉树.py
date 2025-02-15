#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-15 16:32
FileName: P0654. 最大二叉树
Description:
"""
from typing import List, Optional

from icecream import ic

from utils.node import TreeNode


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def create(left, right):
            if left >= right:
                return
            maximum = max(nums[left:right])
            index = nums.index(maximum)
            ic(maximum, index)
            return TreeNode(maximum, create(left, index), create(index + 1, right))

        return create(0, len(nums))


if __name__ == '__main__':
    solution = Solution().constructMaximumBinaryTree(nums=[3, 2, 1, 6, 0, 5])
    ic(solution.__str__())
