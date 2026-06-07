#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-07 20:23
FileName: P1662. 检查两个字符串数组是否相等.py
Description:
"""
from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return ''.join(word1) == ''.join(word2)


if __name__ == '__main__':
    solution = Solution().arrayStringsAreEqual(word1 = ["ab", "c"], word2 = ["a", "bc"])
    print(solution)
