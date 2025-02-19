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
            if i - k < 0:
                a = 0
            else:
                a = nums[i - k]
            try:
                b = nums[i + k]
            except IndexError:
                b = 0
            if num > a and num > b:
                ss += num
        return ss


if __name__ == '__main__':
    solution = Solution().sumOfGoodNumbers(nums=[1, 3, 2, 1, 5, 4], k=2)
    ic(solution)
