#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-02-28 22:05
FileName: P3842. 切换打开灯泡.py
Description:
"""

from collections import Counter


class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        counter = Counter(bulbs)
        return sorted(k for k, v in counter.items() if v % 2 == 1)


if __name__ == '__main__':
    s = Solution().toggleLightBulbs(bulbs=[10, 30, 20, 10])
    print(s)
