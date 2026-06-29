#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-28 21:30
FileName: P2843. 统计对称整数的数目.py
Description:
"""


class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        nums = []
        for num in range(low, high + 1):
            digits = [int(digit) for digit in str(num)]
            if len(digits) % 2 != 0:
                continue
            if sum(digits[:len(digits) // 2]) == sum(digits[len(digits) // 2:]):
                nums.append(num)
        return len(nums)


if __name__ == '__main__':
    solution = Solution().countSymmetricIntegers(1200, 1230)
    print(solution)
