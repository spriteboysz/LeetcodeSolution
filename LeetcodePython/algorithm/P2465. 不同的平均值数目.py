#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-25 11:43
FileName: P2465. 不同的平均值数目
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        return len({nums[i] + nums[-1 - i] for i in range(len(nums) // 2)})


if __name__ == '__main__':
    solution = Solution().distinctAverages(nums=[4, 1, 4, 0, 3, 5])
    ic(solution)
