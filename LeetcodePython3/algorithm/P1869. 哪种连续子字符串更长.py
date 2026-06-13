#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-13 13:31
FileName: P1869. 哪种连续子字符串更长.py
Description:
"""
from collections import defaultdict


class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        s = s.replace('01', '0#1').replace('10', '1#0')
        dic = defaultdict(int)
        for word in s.split('#'):
            dic[word[0]] = max(dic[word[0]], len(word))
        return dic.get('1', 0) > dic.get('0', 0)


if __name__ == '__main__':
    solution = Solution().checkZeroOnes(s="110100010")
    print(solution)
