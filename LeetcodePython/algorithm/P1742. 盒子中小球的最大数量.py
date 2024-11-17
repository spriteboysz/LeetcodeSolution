#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-17 20:55
FileName: P1742. 盒子中小球的最大数量
Description:
"""
from collections import defaultdict


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        dic = defaultdict(int)
        for i in range(lowLimit, highLimit + 1):
            dic[sum(map(int, list(str(i))))] += 1
        return max(dic.values())


if __name__ == '__main__':
    solution = Solution().countBalls(1, 10)
    print(solution)
