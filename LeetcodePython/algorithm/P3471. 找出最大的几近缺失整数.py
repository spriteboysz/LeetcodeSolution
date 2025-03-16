#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-16 22:33
FileName: algorithm/P3471. 找出最大的几近缺失整数.py
Description: 
"""
from collections import Counter
from typing import List

from icecream import ic


class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        if k == len(nums):
            return max(nums)
        counter = Counter(nums)
        if k == 1:
            keys = [k for k, v in counter.items() if v == 1]
            return max(keys) if keys else -1
        head, tail = nums[0], nums[-1]
        if counter[head] == counter[tail] == 1:
            return max(head, tail)
        if counter[head] == 1:
            return head
        if counter[tail] == 1:
            return tail
        return -1


if __name__ == '__main__':
    solution = Solution().largestInteger(nums=[3, 9, 2, 1, 7], k=3)
    ic(solution)
