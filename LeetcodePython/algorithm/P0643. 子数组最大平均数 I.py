#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-08 11:22
FileName: P0643. 子数组最大平均数 I
Description:
"""
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        acc = maximum = sum(nums[:k])
        for i in range(k, len(nums)):
            acc += nums[i]
            acc -= nums[i - k]
            maximum = max(maximum, acc)
        return maximum / k


if __name__ == '__main__':
    solution = Solution().findMaxAverage(nums=[1, 12, -5, -6, 50, 3], k=4)
    print(solution)
