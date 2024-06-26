#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-04-27 13:35
FileName: algorithm
Description:P2383. 赢得比赛需要的最少训练时长.py 
"""
from typing import List


class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int],
                         experience: List[int]) -> int:
        cnt, total = 0, sum(energy)
        if initialEnergy <= total:
            cnt += (total - initialEnergy + 1)
        for exp in experience:
            if initialExperience <= exp:
                cnt += (exp - initialExperience + 1)
                initialExperience = exp + 1
            initialExperience += exp
        return cnt


if __name__ == '__main__':
    print(
        Solution().minNumberOfHours(initialEnergy=5, initialExperience=3, energy=[1, 4, 3, 2], experience=[2, 6, 3, 1]))
