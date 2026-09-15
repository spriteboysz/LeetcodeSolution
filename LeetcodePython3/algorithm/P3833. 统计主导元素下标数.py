#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-14 14:32
FileName: algorithm/P3833. 统计主导元素下标数.py
Description: 
"""
from typing import List


class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        suffixes, acc = [], 0
        for num in nums[::-1]:
            acc += num
            suffixes.append(acc)
        suffixes.reverse()

        cnt = 0
        for i, num in enumerate(nums[:-1]):
            if num * (len(nums) - i - 1) > suffixes[i + 1]:
                cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().dominantIndices([5, 4, 3])
    print('<None>' if solution is None else f'{solution=}')
