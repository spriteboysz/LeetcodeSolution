#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-01 20:37
FileName: LCR 004. 只出现一次的数字 II
Description:
"""

from collections import Counter
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)
        return [num for num, cnt in counter.items() if cnt == 1][0]


if __name__ == '__main__':
    solution = Solution().singleNumber([0, 1, 0, 1, 0, 1, 100])
    print(solution)
