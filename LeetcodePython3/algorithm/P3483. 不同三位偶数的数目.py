#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-28 19:56
FileName: P3483. 不同三位偶数的数目.py
Description:
"""
from typing import List, Counter


class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        counter = Counter(digits)
        nums = []
        for num in range(100, 999, 2):
            counter1 = counter.copy()
            for digit in str(num):
                counter1[int(digit)] -= 1
            if all(v >= 0 for v in counter1.values()):
                nums.append(num)
        return len(nums)


if __name__ == '__main__':
    solution = Solution().totalNumbers(digits=[1, 2, 3, 4])
    print(solution)
