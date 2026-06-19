#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-19 11:26
FileName: P2423. 删除字符使频率相同.py
Description:
"""
from collections import Counter


class Solution:
    def equalFrequency(self, word: str) -> bool:
        counter = Counter(word)
        for ch, cnt in counter.items():
            counter1 = counter.copy()
            counter1[ch] -= 1
            if counter1[ch] == 0:
                counter1.pop(ch)
            if len(set(counter1.values())) == 1:
                return True
        return False


if __name__ == '__main__':
    solution = Solution().equalFrequency('abc')
    print(solution)
