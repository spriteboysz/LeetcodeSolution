#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-15 11:19
FileName: algorithm/P3913. 按频率对元音排序.py
Description: 
"""
from collections import defaultdict


class Solution:
    def sortVowels(self, s: str) -> str:
        dic = defaultdict(list)
        for i, ch in enumerate(s):
            if ch in 'aeiou':
                dic[ch].append(i)
        vowels = sorted(dic, key=lambda c: (-len(dic.get(c, [])), dic.get(c, [])[0]))
        vowels = list(''.join(c * len(dic.get(c, [])) for c in vowels))[::-1]

        ss = list(s)
        for i, ch in enumerate(ss):
            if ch in 'aeiou':
                ss[i] = vowels.pop()
        return ''.join(ss)


if __name__ == '__main__':
    solution = Solution().sortVowels(s="leetcode")
    print(solution)
