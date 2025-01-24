#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-24 21:46
FileName: P1480. 一维数组的动态和
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running, acc = [], 0
        for num in nums:
            acc += num
            running.append(acc)
        return running


if __name__ == '__main__':
    solution = Solution().runningSum(nums=[3, 1, 2, 10, 1])
    ic(solution)
