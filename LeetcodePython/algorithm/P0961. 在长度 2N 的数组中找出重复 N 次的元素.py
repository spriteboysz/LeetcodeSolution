#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-28 23:04
FileName: P0961. 在长度 2N 的数组中找出重复 N 次的元素
Description:
"""
from typing import List
from collections import Counter


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        counter = Counter(nums)
        for k, v in counter.items():
            if v == len(nums) // 2:
                return k
        return -1


if __name__ == '__main__':
    solution = Solution().repeatedNTimes(nums=[5, 1, 5, 2, 5, 3, 5, 4])
    print(solution)
