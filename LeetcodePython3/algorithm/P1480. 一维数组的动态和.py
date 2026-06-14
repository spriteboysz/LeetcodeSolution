#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-14 18:58
FileName: P1480. 一维数组的动态和.py
Description:
"""
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running, acc = [], 0
        for num in nums:
            acc += num
            running.append(acc)
        return running


if __name__ == '__main__':
    solution = Solution().runningSum([1, 2, 3, 4])
    print(solution)
