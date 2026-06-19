#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-19 11:19
FileName: P2287. 重排字符形成目标字符串.py
Description:
"""
from collections import Counter


class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        counter1, counter2 = Counter(s), Counter(target)
        return min(counter1.get(ch, 0) // cnt for ch, cnt in counter2.items())


if __name__ == '__main__':
    solution = Solution().rearrangeCharacters(s="ilovecodingonleetcode", target="code")
    print(solution)
