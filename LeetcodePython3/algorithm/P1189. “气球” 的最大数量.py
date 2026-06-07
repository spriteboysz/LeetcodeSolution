#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-07 17:08
FileName: P1189. “气球” 的最大数量.py
Description:
"""
from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = Counter(text)
        cnt = len(text)
        for ch in 'ban':
            cnt = min(cnt, counter.get(ch, 0))
        for ch in 'lo':
            cnt = min(cnt, counter.get(ch, 0) // 2)
        return cnt


if __name__ == '__main__':
    solution = Solution().maxNumberOfBalloons(text="loonbalxballpoon")
    print(solution)
