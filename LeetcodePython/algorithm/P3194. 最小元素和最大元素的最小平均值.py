#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-24 12:15
FileName: P3194. 最小元素和最大元素的最小平均值
Description:
"""
from typing import List


class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        n = len(nums)
        return min([nums[i] + nums[n - 1 - i] for i in range(n // 2)]) / 2


if __name__ == '__main__':
    solution = Solution().minimumAverage(nums=[7, 8, 3, 4, 15, 13, 4, 1])
    print(solution)
