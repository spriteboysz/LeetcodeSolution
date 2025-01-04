#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-04 21:38
FileName: P2206. 将数组划分成相等数对
Description:
"""
from collections import Counter
from typing import List

from icecream import ic


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        return all(cnt % 2 == 0 for cnt in counter.values())


if __name__ == '__main__':
    solution = Solution().divideArray(nums=[3, 2, 3, 2, 2, 2])
    ic(solution)
