#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-10 22:10
FileName: P3982. 最大数字范围的整数之和.py
Description:
"""
from collections import defaultdict


class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        dic = defaultdict(int)
        for num in nums:
            digits = [int(digit) for digit in str(num)]
            dic[max(digits) - min(digits)] += num
        return dic.get(max(dic), 0)


if __name__ == '__main__':
    solution = Solution().maxDigitRange(nums=[5724, 111, 350])
    print(solution)
