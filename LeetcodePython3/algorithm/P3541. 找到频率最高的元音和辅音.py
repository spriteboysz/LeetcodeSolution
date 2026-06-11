#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-11 22:50
FileName: P3541. 找到频率最高的元音和辅音.py
Description:
"""

from collections import Counter


class Solution:
    def maxFreqSum(self, s: str) -> int:
        counter = Counter(s)
        cnt1, cnt2 = [], []
        for ch, cnt in counter.items():
            if ch in 'aeiou':
                cnt1.append(cnt)
            else:
                cnt2.append(cnt)
        return max(cnt1, default=0) + max(cnt2, default=0)


if __name__ == '__main__':
    solution = Solution().maxFreqSum(s="successes")
    print(solution)
