#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-02 08:48
FileName: algorithm/P3847. 计算比赛分数差.py
Description: 
"""
from typing import List


class Solution:
    def scoreDifference(self, nums: List[int]) -> int:
        scores, pos = [0, 0], 0
        for i, num in enumerate(nums):
            if num % 2 == 1:
                pos = 1 - pos
            if i % 6 == 5:
                pos = 1 - pos
            scores[pos] += num
        return scores[0] - scores[1]


if __name__ == '__main__':
    solution = Solution().scoreDifference(nums=[2, 4, 2, 1, 2, 1])
    print(solution)
