#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-14 13:58
FileName: algorithm/P4048. 统计等间距出现整数数目 I.py
Description: 
"""
from collections import defaultdict


class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        dic = defaultdict(list)
        for i, num in enumerate(nums):
            dic[num].append(i)
        cnt = 0
        for k, v in dic.items():
            if len(v) != 3:
                continue
            if v[2] - v[1] == v[1] - v[0]:
                cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().countSpecialIntegers(nums=[1, 8, 1, 5, 1, 5, 8, 5])
    print('<None>' if solution is None else f'{solution=}')
