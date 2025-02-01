#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-31 23:10
FileName: P1624. 两个相同字符之间的最长子字符串
Description:
"""
from collections import defaultdict
from string import ascii_lowercase

from icecream import ic


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        dic = defaultdict(list)
        for i, ch in enumerate(s):
            dic[ch].append(i)
        maximum = -1
        for ch in ascii_lowercase:
            if len(dic[ch]) >= 2:
                maximum = max(maximum, dic[ch][-1] - dic[ch][0])
        return maximum - 1 if maximum != -1 else -1


if __name__ == '__main__':
    solution = Solution().maxLengthBetweenEqualCharacters('abca')
    ic(solution)
