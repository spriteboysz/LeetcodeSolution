#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-27 23:09
FileName: P0409. 最长回文串
Description:
"""
from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        cnt1, cnt2 = 0, 0
        for k, v in counter.items():
            if v % 2 == 1:
                cnt1 |= 1
            cnt2 += v // 2
        return cnt1 + cnt2 * 2


if __name__ == '__main__':
    solution = Solution().longestPalindrome(s="abccccdd")
    print(solution)
