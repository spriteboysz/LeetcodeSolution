#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-24 12:24
FileName: P3010. 将数组分成最小总代价的子数组 I
Description:
"""
from typing import List


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        return sum(sorted(nums[1:])[:2]) + nums[0]

if __name__ == '__main__':
    solution = Solution().minimumCost(nums = [1,2,3,12])
    print(solution)