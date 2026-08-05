#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-04 23:13
FileName: P4006. 统计有效前缀数目.py
Description:
"""


class Solution:
    def countValidPrefixes(self, s: str) -> int:
        cnt, cnt0, cnt1 = 0, 0, 0
        for ch in s:
            if ch == '0':
                cnt0 += 1
            else:
                cnt1 += 1
            if abs(cnt0 - cnt1) <= 1:
                cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().countValidPrefixes(s="101")
    print(solution)
