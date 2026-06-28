#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-27 22:49
FileName: P1399. 统计最大组的数目.py
Description:
"""
from collections import defaultdict


class Solution:
    def countLargestGroup(self, n: int) -> int:
        dic = defaultdict(int)
        for num in range(1, n + 1):
            dic[sum(int(digit) for digit in str(num))] += 1
        maximum = max(dic.values())
        return sum(v == maximum for v in dic.values())


if __name__ == '__main__':
    solution = Solution().countLargestGroup(13)
    print(solution)
