#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-20 11:21
FileName: P2094. 找出 3 位偶数.py
Description:
"""
from typing import List, Counter


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        nums = []
        counter = Counter(digits)
        for i in range(100, 999, 2):
            counter1 = counter.copy()
            for digit in map(int, str(i)):
                counter1[digit] -= 1
                if counter1[digit] < 0:
                    break
            else:
                nums.append(i)
        return nums


if __name__ == '__main__':
    solution = Solution().findEvenNumbers(digits=[2, 1, 3, 0])
    print(solution)
