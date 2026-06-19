#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-19 20:55
FileName: P2535. 数组元素和与数字和的绝对差.py
Description:
"""
from typing import List


class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        return abs(sum(int(digit) for num in nums for digit in str(num)) - sum(nums))


if __name__ == '__main__':
    solution = Solution().differenceOfSum([1, 15, 6, 3])
    print(solution)
