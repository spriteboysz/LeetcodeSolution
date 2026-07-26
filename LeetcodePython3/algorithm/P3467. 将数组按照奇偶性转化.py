#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-26 11:35
FileName: P3467. 将数组按照奇偶性转化.py
Description:
"""
from typing import List


class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        odd, even = 0, 0
        for num in nums:
            if num % 2 == 1:
                odd += 1
            else:
                even += 1
        return [0] * even + [1] * odd


if __name__ == '__main__':
    solution = Solution().transformArray(nums=[1, 5, 1, 4, 2])
    print(solution)
