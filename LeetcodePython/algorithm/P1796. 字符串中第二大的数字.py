#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-24 22:33
FileName: P1796. 字符串中第二大的数字
Description:
"""
import re


class Solution:
    def secondHighest(self, s: str) -> int:
        matches = re.findall(r'(\d)', s)
        digits = list(map(int, set(matches)))
        if len(digits) < 2:
            return -1
        return sorted(digits, reverse=True)[1]


if __name__ == '__main__':
    solution = Solution().secondHighest(s="dfa12321afd")
    print(solution)
