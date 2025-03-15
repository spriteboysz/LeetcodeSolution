#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-15 19:43
FileName: algorithm/P2399. 检查相同字母间的距离.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        dic = dict()
        for i, ch in enumerate(s):
            if ch in dic:
                dic[ch] = i - dic[ch] - 1
            else:
                dic[ch] = i
        return all(distance[ord(ch) - ord('a')] == d for ch, d in dic.items())


if __name__ == '__main__':
    solution = Solution().checkDistances(
        s="abaccb",
        distance=[1, 3, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    ic(solution)
