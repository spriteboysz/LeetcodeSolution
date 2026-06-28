#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-27 22:09
FileName: P0228. 汇总区间.py
Description:
"""
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        if not nums:
            return ranges

        nums.append(nums[-1] + 2)
        left = curr = nums[0]
        for i, num in enumerate(nums[1:], start=1):
            if num - curr != 1:
                ranges.append(f'{left}->{nums[i - 1]}' if nums[i - 1] - left >= 1 else f'{nums[i - 1]}')
                left = curr = nums[i]
            else:
                curr = nums[i]
        return ranges


if __name__ == '__main__':
    solution = Solution().summaryRanges(nums=[-3, -2])
    print(solution)
