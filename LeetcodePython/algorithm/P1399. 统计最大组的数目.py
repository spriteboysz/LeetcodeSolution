#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-31 22:18
FileName: P1399. 统计最大组的数目
Description:
"""
from collections import defaultdict

from icecream import ic


class Solution:
    def countLargestGroup(self, n: int) -> int:
        dic = defaultdict(list)
        for i in range(1, n + 1):
            dic[sum(map(int, str(i)))].append(i)
        maximum = max(map(len, dic.values()))
        return sum(len(el) == maximum for el in dic.values())


if __name__ == '__main__':
    solution = Solution().countLargestGroup(13)
    ic(solution)
