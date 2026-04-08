#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-04-07 23:12
FileName: P3849. 重新排列后的最大按位异或值.py
Description:
"""


class Solution:
    def maximumXor(self, s: str, t: str) -> str:
        cnt0, cnt1 = t.count('0'), t.count('1')
        ss = ''
        for ch in s:
            if ch == '0' and cnt1 > 0:
                ss += '1'
                cnt1 -= 1
            elif ch == '0':
                ss += '0'
                cnt0 -= 1
            elif ch == '1' and cnt0 > 0:
                ss += '1'
                cnt0 -= 1
            else:
                ss += '0'
                cnt1 -= 1
        return ss


if __name__ == '__main__':
    solution = Solution().maximumXor(s="0110", t="1110")
    print(solution)
