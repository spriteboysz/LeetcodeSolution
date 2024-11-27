#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-26 22:58
FileName: P1748. 唯一元素的和
Description:
"""
from typing import List
from collections import Counter


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counter = Counter(nums)
        return sum([num for num, cnt in counter.items() if cnt == 1])


if __name__ == '__main__':
    solution = Solution().sumOfUnique(nums=[1, 2, 3, 2, 1, 3])
    print(solution)
