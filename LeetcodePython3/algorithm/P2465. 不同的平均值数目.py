#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-20 16:41
FileName: P2465. 不同的平均值数目.py
Description:
"""
from typing import List


class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        distinct = set()
        nums.sort()
        for i in range(len(nums) // 2):
            distinct.add(nums[i] + nums[-1 - i])
        return len(distinct)


if __name__ == '__main__':
    solution = Solution().distinctAverages(nums=[4, 1, 4, 0, 3, 5])
    print(solution)
