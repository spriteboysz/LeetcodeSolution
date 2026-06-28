#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-28 11:17
FileName: P2367. 等差三元组的数目.py
Description:
"""
from typing import List


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        seen = set(nums)
        return sum((num + diff) in seen and (num + diff * 2) in seen for num in nums)


if __name__ == '__main__':
    solution = Solution().arithmeticTriplets(nums=[0, 1, 4, 6, 7, 10], diff=3)
    print(solution)
