#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-02 22:50
FileName: P2788. 按分隔符拆分字符串
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        return [word for word in sum([word.split(separator) for word in words], []) if word]


if __name__ == '__main__':
    solution = Solution().splitWordsBySeparator(words=["one.two.three", "four.five", "six"], separator=".")
    ic(solution)
