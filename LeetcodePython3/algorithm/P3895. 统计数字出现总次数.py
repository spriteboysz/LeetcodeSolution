#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-08 23:09
FileName: P3895. 统计数字出现总次数.py
Description:
"""


class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        return ''.join(map(str, nums)).count(str(digit))


if __name__ == '__main__':
    solution = Solution().countDigitOccurrences(nums = [12,54,32,22], digit = 2)
    print(solution)
