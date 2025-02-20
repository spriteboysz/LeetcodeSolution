#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-19 22:56
FileName: P3452. 好数字之和
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        ss = 0
        for i, num in enumerate(nums):
            a = nums[i - k] if i - k >= 0 else 0
            b = nums[i + k] if i + k < len(nums) else 0
            if num > a and num > b:
                ss += num
        return ss


if __name__ == '__main__':
    solution = Solution().sumOfGoodNumbers(nums=[1, 3, 2, 1, 5, 4], k=2)
    ic(solution)
