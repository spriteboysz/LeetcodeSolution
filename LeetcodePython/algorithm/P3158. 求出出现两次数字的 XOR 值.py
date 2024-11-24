#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-24 21:02
FileName: P3158. 求出出现两次数字的 XOR 值
Description:
"""
from functools import reduce
from typing import List
from collections import Counter


class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        counter = Counter(nums)
        nums1 = [num for num, cnt in counter.items() if cnt == 2]
        return reduce(lambda num1, num2: num1 ^ num2, nums1, 0)


if __name__ == '__main__':
    solution = Solution().duplicateNumbersXOR(nums=[1, 2, 2, 1])
    print(solution)
