#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-27 22:56
FileName: algorithm/P2191. 将杂乱无章的数字排序.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def calc(num):
            ret = 0
            for digit in str(num):
                ret = ret * 10 + mapping[int(digit)]
            return ret

        return sorted(nums, key=calc)


if __name__ == '__main__':
    solution = Solution().sortJumbled(mapping=[8, 9, 4, 0, 2, 1, 3, 5, 7, 6], nums=[991, 338, 38])
    ic(solution)
