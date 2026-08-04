#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-01 16:02
FileName: P2006. 差的绝对值为 K 的数对数目.py
Description:
"""
from typing import List


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        cnt = 0
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums[i + 1:], start=i + 1):
                if abs(num1 - num2) == k:
                    cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().countKDifference([1, 2, 2, 1], 1)
    print(solution)
