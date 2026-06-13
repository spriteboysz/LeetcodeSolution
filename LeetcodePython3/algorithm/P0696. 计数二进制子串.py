#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-13 12:39
FileName: P0696. 计数二进制子串.py
Description:
"""
from itertools import pairwise


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        s = s.replace('01', '0#1').replace('10', '1#0')
        segments = [len(seg) for seg in s.split('#')]
        return sum(min(cnt1, cnt2) for cnt1, cnt2 in pairwise(segments))


if __name__ == '__main__':
    solution = Solution().countBinarySubstrings(s="00110011")
    print(solution)
