#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-10 22:43
FileName: P3842. 切换打开灯泡.py
Description:
"""
from collections import defaultdict


class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        dic = defaultdict(int)
        for bulb in bulbs:
            dic[bulb] += 1
        return sorted([bulb for bulb in dic if dic.get(bulb, 0) % 2 == 1])


if __name__ == '__main__':
    solution = Solution().toggleLightBulbs(bulbs=[10, 30, 20, 10])
    print(solution)
