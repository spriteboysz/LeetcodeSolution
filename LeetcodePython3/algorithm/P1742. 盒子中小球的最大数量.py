#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-28 10:59
FileName: P1742. 盒子中小球的最大数量.py
Description:
"""
from collections import defaultdict


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        dic = defaultdict(int)
        for num in range(lowLimit, highLimit + 1):
            dic[sum(int(digit) for digit in str(num))] += 1
        return max(dic.values())


if __name__ == '__main__':
    solution = Solution().countBalls(1, 10)
    print(solution)
