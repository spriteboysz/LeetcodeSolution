#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-15 10:40
FileName: algorithm/P3121. 统计特殊字母的数量 II.py
Description: 
"""
from collections import defaultdict


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        dic = defaultdict(list)
        for i, ch in enumerate(word):
            dic[ch].append(i)
        cnt = 0
        for ch, v in dic.items():
            if ch.isupper() or ch.upper() not in dic:
                continue
            if v[-1] < dic.get(ch.upper(), [])[0]:
                cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().numberOfSpecialChars(word="aaAbcBC")
    print(solution)
