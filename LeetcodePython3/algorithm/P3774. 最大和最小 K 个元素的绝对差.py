#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-30 23:00
FileName: P3774. 最大和最小 K 个元素的绝对差.py
Description:
"""
from typing import List


class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return sum(nums[:k]) - sum(nums[-k:])


if __name__ == '__main__':
    solution = Solution().absDifference(nums=[5, 2, 2, 4], k=2)
    print(solution)
