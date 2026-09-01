#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-01 09:05
FileName: algorithm/P3028. 边界上的蚂蚁.py
Description: 
"""
from typing import List


class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        cnt, pos = 0, 0
        for num in nums:
            pos += num
            if pos == 0:
                cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().returnToBoundaryCount(nums=[3, 2, -3, -4])
    print(solution)
