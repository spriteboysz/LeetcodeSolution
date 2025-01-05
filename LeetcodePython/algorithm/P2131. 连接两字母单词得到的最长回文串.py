#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-05 12:48
FileName: P2131. 连接两字母单词得到的最长回文串
Description:
"""
from collections import Counter
from typing import List

from icecream import ic


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        counter = Counter(words)
        cnt1, cnt2, mid = 0, 0, 0
        for k, v in counter.items():
            if k[0] == k[1]:
                cnt1 += v // 2
                if v % 2 == 1:
                    mid = 2
            else:
                cnt2 += min(v, counter.get(k[::-1], 0))
        return cnt2 * 2 + cnt1 * 4 + mid


if __name__ == '__main__':
    solution = Solution().longestPalindrome(["ab", "ty", "yt", "lc", "cl", "ab"])
    ic(solution)
