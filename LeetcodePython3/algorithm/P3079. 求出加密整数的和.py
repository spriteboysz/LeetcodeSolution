#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-20 18:53
FileName: P3079. 求出加密整数的和.py
Description:
"""
from typing import List


class Solution:
    @staticmethod
    def calc(num: int):
        digits = [int(digit) for digit in str(num)]
        maximum = max(digits)
        return int(str(maximum) * len(digits))

    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        return sum(self.calc(num) for num in nums)


if __name__ == '__main__':
    solution = Solution().sumOfEncryptedInt(nums=[10, 21, 31])
    print(solution)
