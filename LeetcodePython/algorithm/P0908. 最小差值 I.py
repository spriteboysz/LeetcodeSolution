#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-17 18:30
FileName: P0908. 最小差值 I
Description:
"""
from typing import List


class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        maximum, minimum = max(nums), min(nums)
        return max(maximum - k - (minimum + k), 0)


if __name__ == '__main__':
    solution = Solution().smallestRangeI(nums=[1, 3, 6], k=3)
    print(solution)
