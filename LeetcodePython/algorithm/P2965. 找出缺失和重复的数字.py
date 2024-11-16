#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-16 11:38
FileName: P2965. 找出缺失和重复的数字
Description:
"""
from typing import List
from collections import Counter


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        nums = [num for row in grid for num in row]
        counter = Counter(nums)
        repeat, miss = -1, -1
        for num in range(len(nums) ** 2):
            if counter.get(num + 1, 0) == 2:
                repeat = num + 1
            if counter.get(num + 1, 0) == 0:
                miss = num + 1
            if repeat != -1 and miss != -1:
                break
        return [repeat, miss]


if __name__ == '__main__':
    solution = Solution().findMissingAndRepeatedValues([[9, 1, 7], [8, 9, 2], [3, 4, 6]])
    print(solution)
