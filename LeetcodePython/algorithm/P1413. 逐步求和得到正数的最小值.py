#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-31 22:28
FileName: P1413. 逐步求和得到正数的最小值
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minimum, acc = nums[0], 0
        for num in nums:
            acc += num
            minimum = min(minimum, acc)
        return max(1, 1 - minimum)


if __name__ == '__main__':
    solution = Solution().minStartValue([-3, 2, -3, 4, 2])
    ic(solution)
