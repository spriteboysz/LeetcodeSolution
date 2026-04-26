#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-04-26 19:25
FileName: P3895. 统计数字出现总次数.py
Description:
"""

from collections import Counter


class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        return sum(Counter(str(num)).get(str(digit), 0) for num in nums)


if __name__ == '__main__':
    solution = Solution().countDigitOccurrences(nums=[12, 54, 32, 22], digit=2)
    print(solution)
