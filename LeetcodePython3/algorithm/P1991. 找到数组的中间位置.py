#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-28 17:34
FileName: P1991. 找到数组的中间位置.py
Description:
"""
from typing import List


class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total, acc = sum(nums), 0
        for i, num in enumerate(nums):
            acc += num
            if (acc - num) * 2 + num == total:
                return i
        return -1


if __name__ == '__main__':
    solution = Solution().findMiddleIndex(nums=[2, 3, -1, 8, 4])
    print(solution)
