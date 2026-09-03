#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-01 12:02
FileName: LC/P2966. 划分数组并满足最大差限制.py
Description: 
"""
from typing import List


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        divide = [nums[i:i + 3] for i in range(0, len(nums), 3)]
        if any(d[-1] - d[0] > k for d in divide):
            return []
        return divide


if __name__ == '__main__':
    solution = Solution().divideArray(
        nums=[4, 2, 9, 8, 2, 12, 7, 12, 10, 5, 8, 5, 5, 7, 9, 2, 5, 11], k=14
    )
    print(solution)
