#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-04-26 20:53
FileName: P3659. 数组元素分组.py
Description:
"""
from collections import Counter
from typing import List


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False
        return max(Counter(nums).values()) * k <= len(nums)


if __name__ == '__main__':
    solution = Solution().partitionArray(nums=[1, 2, 3, 4], k=2)
    print(solution)
