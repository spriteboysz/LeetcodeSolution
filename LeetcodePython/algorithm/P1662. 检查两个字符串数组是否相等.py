#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-31 23:23
FileName: P1662. 检查两个字符串数组是否相等
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return ''.join(word1) == ''.join(word2)


if __name__ == '__main__':
    solution = Solution().arrayStringsAreEqual(word1=["ab", "c"], word2=["a", "bc"])
    ic(solution)
