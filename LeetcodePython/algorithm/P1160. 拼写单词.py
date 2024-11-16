#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-16 13:57
FileName: P1160. 拼写单词
Description:
"""
from typing import List
from collections import Counter


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        counter = Counter(chars)
        cnt = 0
        for word in words:
            if all([v <= counter.get(k, 0) for k, v in Counter(word).items()]):
                cnt += len(word)
        return cnt


if __name__ == '__main__':
    solution = Solution().countCharacters(words=["cat", "bt", "hat", "tree"], chars="atach")
    print(solution)
