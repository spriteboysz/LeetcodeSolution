#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-12 23:22
FileName: P1347. 制造字母异位词的最小步骤数
Description:
"""

from icecream import ic


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        alphabet = [0] * 26
        for ch1, ch2 in zip(s, t):
            alphabet[ord(ch1) - ord('a')] += 1
            alphabet[ord(ch2) - ord('a')] -= 1
        return sum(map(abs, alphabet)) // 2


if __name__ == '__main__':
    solution = Solution().minSteps(s="leetcode", t="practice")
    ic(solution)
