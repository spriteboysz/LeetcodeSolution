#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-20 16:38
FileName: P2553. 分割数组中数字的数位.py
Description:
"""
from typing import List


class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        return sum([list(map(int, str(num))) for num in nums], [])


if __name__ == '__main__':
    solution = Solution().separateDigits(nums=[13, 25, 83, 77])
    print(solution)
