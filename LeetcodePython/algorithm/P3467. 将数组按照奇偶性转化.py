#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-02 23:00
FileName: algorithm/P3467. 将数组按照奇偶性转化.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        cnt = sum(num % 2 == 0 for num in nums)
        return [0] * cnt + [1] * (len(nums) - cnt)


if __name__ == '__main__':
    solution = Solution().transformArray(nums=[4, 3, 2, 1])
    ic(solution)
