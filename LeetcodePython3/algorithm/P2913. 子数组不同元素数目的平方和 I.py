#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-02 08:54
FileName: algorithm/P2913. 子数组不同元素数目的平方和 I.py
Description: 
"""
from typing import List


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        cnt, n = 0, len(nums)
        for i in range(n + 1):
            for j in range(i):
                cnt += len(set(nums[j:i])) ** 2
        return cnt


if __name__ == '__main__':
    solution = Solution().sumCounts([1, 2, 1])
    print(solution)
