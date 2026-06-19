#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-18 23:36
FileName: P1624. 两个相同字符之间的最长子字符串.py
Description:
"""

from collections import defaultdict
from string import ascii_lowercase as lowercase


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        dic = defaultdict(list)
        for i, ch in enumerate(s):
            dic[ch].append(i)
        return max([dic[ch][-1] - dic[ch][0] - 1 for ch in lowercase if len(dic[ch]) >= 2], default=-1)


if __name__ == '__main__':
    solution = Solution().maxLengthBetweenEqualCharacters(s="cabbac")
    print(solution)
