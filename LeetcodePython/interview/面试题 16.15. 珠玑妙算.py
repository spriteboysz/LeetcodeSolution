#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-23 23:13
FileName: 面试题 16.15. 珠玑妙算
Description:
"""
from collections import defaultdict
from typing import List


class Solution:
    def masterMind(self, solution: str, guess: str) -> List[int]:
        a, b = 0, 0
        dic1, dic2 = defaultdict(int), defaultdict(int)
        for ch1, ch2 in zip(solution, guess):
            if ch1 == ch2:
                a += 1
            else:
                dic1[ch1] += 1
                dic2[ch2] += 1
        for color in ['R', 'Y', 'G', 'B']:
            b += min(dic1[color], dic2[color])
        return [a, b]


if __name__ == '__main__':
    solution = Solution().masterMind(solution="RGBY", guess="GGRR")
    print(solution)
