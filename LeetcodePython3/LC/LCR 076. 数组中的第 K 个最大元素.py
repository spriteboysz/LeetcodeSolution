#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-07 14:39
FileName: 面试题/LCR 076. 数组中的第 K 个最大元素.py
Description: 
"""
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k - 1]


if __name__ == '__main__':
    solution = Solution().findKthLargest(nums=[3, 2, 1, 5, 6, 4], k=2)
    print('<None>' if not solution else f'{solution=}')
