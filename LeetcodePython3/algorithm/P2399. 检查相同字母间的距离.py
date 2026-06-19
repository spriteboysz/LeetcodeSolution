#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-19 08:34
FileName: P2399. 检查相同字母间的距离.py
Description:
"""
from typing import List


class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        dic = {}
        for i, ch in enumerate(s):
            if ch not in dic:
                dic[ch] = i
            else:
                dic[ch] = i - dic[ch] - 1
        return all(d == distance[ord(ch) - ord('a')] for ch, d in dic.items())


if __name__ == '__main__':
    solution = Solution().checkDistances(
        s="abaccb",
        distance=[1, 3, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    )
    print(solution)
