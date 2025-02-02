#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-01 21:48
FileName: P1974. 使用特殊打字机键入单词的最少时间
Description:
"""

from icecream import ic


class Solution:
    def minTimeToType(self, word: str) -> int:
        curr = 'a'
        cnt = 0
        for ch in word:
            m = (ord(ch) - ord(curr) + 26) % 26
            cnt += min(m, 26 - m) + 1
            curr = ch
        return cnt


if __name__ == '__main__':
    solution = Solution().minTimeToType(word="abc")
    ic(solution)
