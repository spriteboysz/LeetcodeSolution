#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-01 21:50
FileName: P1287. 有序数组中出现次数超过25%的元素
Description:
"""
from collections import Counter
from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        counter = Counter(arr)
        maximum = max(counter.values())
        return [k for k, v in counter.items() if v == maximum][0]


if __name__ == '__main__':
    solution = Solution().findSpecialInteger([1, 2, 2, 6, 6, 6, 6, 7, 10])
    print(solution)
