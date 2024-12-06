#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-06 21:16
FileName: P0215. 数组中的第K个最大元素
Description:
"""
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]


if __name__ == '__main__':
    solution = Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], k=4)
    print(solution)
