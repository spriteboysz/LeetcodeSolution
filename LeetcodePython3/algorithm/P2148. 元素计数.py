#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-20 11:36
FileName: P2148. 元素计数.py
Description:
"""
from typing import List


class Solution:
    def countElements(self, nums: List[int]) -> int:
        nums = sorted(nums)
        return sum(num != nums[0] and num != nums[-1] for num in nums)


if __name__ == '__main__':
    solution = Solution().countElements(nums=[11, 7, 2, 15])
    print(solution)
