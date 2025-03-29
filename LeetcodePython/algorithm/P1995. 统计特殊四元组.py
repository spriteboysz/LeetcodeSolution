#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-28 21:11
FileName: algorithm/P1995. 统计特殊四元组.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        cnt, n = 0, len(nums)
        for a in range(n):
            for b in range(a + 1, n):
                for c in range(b + 1, n):
                    for d in range(c + 1, n):
                        if nums[a] + nums[b] + nums[c] == nums[d]:
                            cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().countQuadruplets(nums=[1, 1, 1, 3, 5])
    ic(solution)
