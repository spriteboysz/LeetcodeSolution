#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-07 11:53
FileName: P1160. 拼写单词.py
Description:
"""
from collections import Counter

from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        counter = Counter(chars)
        ans = 0
        for word in words:
            if all(cnt <= counter.get(ch, 0) for ch, cnt in Counter(word).items()):
                ans += len(word)
        return ans


if __name__ == '__main__':
    solution = Solution().countCharacters(words=["cat", "bt", "hat", "tree"], chars="atach")
    print(solution)
