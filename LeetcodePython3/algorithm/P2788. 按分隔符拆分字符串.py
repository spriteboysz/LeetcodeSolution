#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-17 22:41
FileName: P2788. 按分隔符拆分字符串.py
Description:
"""
from typing import List


class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans = sum([word.split(separator) for word in words], [])
        return [word for word in ans if word]


if __name__ == '__main__':
    solution = Solution().splitWordsBySeparator(words=["one.two.three", "four.five", "six"], separator=".")
    print(solution)
