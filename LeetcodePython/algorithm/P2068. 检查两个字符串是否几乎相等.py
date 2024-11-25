#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-25 23:03
FileName: P2068. 检查两个字符串是否几乎相等
Description:
"""
from collections import Counter


class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        cnt1, cnt2 = Counter(word1), Counter(word2)
        return all([abs(cnt1.get(k, 0) - cnt2.get(k, 0)) <= 3 for k in cnt1 + cnt2])


if __name__ == '__main__':
    solution = Solution().checkAlmostEquivalent(word1="abcdeef", word2="abaaacc")
    print(solution)
