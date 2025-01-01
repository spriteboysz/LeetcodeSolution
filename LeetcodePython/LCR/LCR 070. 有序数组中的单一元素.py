#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-01 19:18
FileName: LCR 070. 有序数组中的单一元素
Description:
"""
from collections import Counter
from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        counter = Counter(nums)
        return [num for num, v in counter.items() if v == 1][0]


if __name__ == '__main__':
    solution = Solution().singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8])
    print(solution)
