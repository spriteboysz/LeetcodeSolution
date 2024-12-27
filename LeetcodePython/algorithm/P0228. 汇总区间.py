#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-27 21:45
FileName: P0228. 汇总区间
Description:
"""
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i, n = 0, len(nums)
        ranges = []
        while i < n:
            j = i
            while j + 1 < n and nums[j + 1] == nums[j] + 1:
                j += 1
            ranges.append(str(nums[i]) if i == j else f'{nums[i]}->{nums[j]}')
            i = j + 1
        return ranges



if __name__ == '__main__':
    solution = Solution().summaryRanges([0, 2, 3, 4, 6, 8, 9])
    print(solution)
