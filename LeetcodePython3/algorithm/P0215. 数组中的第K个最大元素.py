#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-18 09:53
FileName: P0215. 数组中的第K个最大元素.py
Description:
"""
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k - 1]


if __name__ == '__main__':
    solution = Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], k=4)
    print(solution)
