#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-03-07 15:27
FileName: P3847. 计算比赛分数差.py
Description:
"""
from typing import List


class Solution:
    def scoreDifference(self, nums: List[int]) -> int:
        scores, active = [0, 0], 0
        for i, num in enumerate(nums):
            if num % 2 == 1:
                active = 1 - active
            if i % 6 == 5:
                active = 1 - active
            scores[active] += num
        return scores[0] - scores[1]


if __name__ == '__main__':
    s = Solution().scoreDifference(nums=[1, 2, 3])
    print(s)
