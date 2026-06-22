#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-21 20:31
FileName: P3289. 数字小镇中的捣蛋鬼.py
Description:
"""
from typing import List, Counter


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        return [num for num, cnt in counter.items() if cnt == 2]


if __name__ == '__main__':
    solution = Solution().getSneakyNumbers(nums=[7, 1, 5, 4, 3, 4, 6, 0, 9, 5, 8, 2])
    print(solution)
