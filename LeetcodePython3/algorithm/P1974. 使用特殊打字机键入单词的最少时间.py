#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-28 17:39
FileName: P1974. 使用特殊打字机键入单词的最少时间.py
Description:
"""


class Solution:
    def minTimeToType(self, word: str) -> int:
        curr, cnt = 'a', len(word)
        for ch in word:
            cnt += min(abs(ord(ch) - ord(curr)), 26 - abs(ord(ch) - ord(curr)))
            curr = ch
        return cnt


if __name__ == '__main__':
    solution = Solution().minTimeToType('abc')
    print(solution)
