#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-23 22:45
FileName: P2094. 找出 3 位偶数
Description:
"""
from typing import List
from collections import Counter


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        nums = []
        counter = Counter(digits)
        for num in range(100, 999, 2):
            counter1 = Counter([num // 100, (num // 10) % 10, num % 10])
            if all([v <= counter[k] for k, v in counter1.items()]):
                nums.append(num)
        return nums


if __name__ == '__main__':
    solution = Solution().findEvenNumbers(digits=[2, 2, 8, 8, 2])
    print(solution)
