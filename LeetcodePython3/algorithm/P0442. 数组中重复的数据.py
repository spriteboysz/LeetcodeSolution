#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-07 23:29
FileName: P0442. 数组中重复的数据.py
Description:
"""
from typing import List, Counter


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        return [num for num, cnt in counter.items() if cnt == 2]


if __name__ == '__main__':
    solution = Solution().findDuplicates(nums=[4, 3, 2, 7, 8, 2, 3, 1])
    print(solution)
