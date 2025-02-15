#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-15 17:15
FileName: P2913. 子数组不同元素数目的平方和 I
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        score = 0
        for cnt in range(1, len(nums) + 1):
            for i in range(len(nums) - cnt + 1):
                score += len(set(nums[i:i + cnt])) ** 2
        return score


if __name__ == '__main__':
    solution = Solution().sumCounts(nums=[1, 2, 1])
    ic(solution)
