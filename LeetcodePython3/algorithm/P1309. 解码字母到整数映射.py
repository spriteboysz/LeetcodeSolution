#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-07 17:15
FileName: P1309. 解码字母到整数映射.py
Description:
"""
import re


class Solution:
    def freqAlphabets(self, s: str) -> str:
        matches = re.findall(r'(\d{2}#|\d)', s)
        return ''.join(chr(int(match.rstrip('#')) - 1 + ord('a')) for match in matches)


if __name__ == '__main__':
    solution = Solution().freqAlphabets(s="13#25#1")
    print(solution)
