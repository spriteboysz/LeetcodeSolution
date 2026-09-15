#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-14 14:15
FileName: algorithm/P3903. 最小稳定下标 I.py
Description: 
"""


class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        maximums = [nums[0]]
        for num in nums[1:]:
            maximums.append(max(num, maximums[-1]))
        minimums = [nums[-1]]
        for num in nums[::-1][1:]:
            minimums.append(min(num, minimums[-1]))
        for i, (maximum, minimum) in enumerate(zip(maximums, minimums[::-1])):
            if maximum - minimum <= k:
                return i
        return -1


if __name__ == '__main__':
    solution = Solution().firstStableIndex(nums=[5, 0, 1, 4], k=3)
    print('<None>' if solution is None else f'{solution=}')
