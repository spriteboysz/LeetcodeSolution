#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-26 23:14
FileName: P2273. 移除字母异位词后的结果数组
Description:
"""
from typing import List


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        sort = [sorted(word) for word in words]
        result = [True] + [sort[i - 1] != sort[i] for i in range(1, len(words))]
        return [word for word, ret in zip(words, result) if ret]


if __name__ == '__main__':
    solution = Solution().removeAnagrams(words=["abba", "baba", "bbaa", "cd", "cd"])
    print(solution)
