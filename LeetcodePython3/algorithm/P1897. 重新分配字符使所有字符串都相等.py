#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-12 22:03
FileName: P1897. 重新分配字符使所有字符串都相等.py
Description:
"""
from collections import Counter

from typing import List


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        counter = Counter(''.join(words))
        return all(cnt % len(words) == 0 for cnt in counter.values())


if __name__ == '__main__':
    solution = Solution().makeEqual(words=["abc", "aabc", "bc"])
    print(solution)
