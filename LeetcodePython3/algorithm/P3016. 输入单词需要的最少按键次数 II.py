#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-02 10:22
FileName: algorithm/P3016. 输入单词需要的最少按键次数 II.py
Description: 
"""
from collections import Counter


class Solution:
    def minimumPushes(self, word: str) -> int:
        counter = Counter(word)
        counts = sorted(counter.values(), reverse=True)
        return sum(sum(counts[k:k + 8]) * (k // 8 + 1) for k in range(0, 26, 8))


if __name__ == '__main__':
    solution = Solution().minimumPushes("aabbccddeeffgghhiiiiii")
    print(solution)
