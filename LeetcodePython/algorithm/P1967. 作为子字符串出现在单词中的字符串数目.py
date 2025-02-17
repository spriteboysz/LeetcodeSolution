#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-15 17:30
FileName: P1967. 作为子字符串出现在单词中的字符串数目
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return sum(pattern in word for pattern in patterns)


if __name__ == '__main__':
    solution = Solution().numOfStrings(patterns=["a", "abc", "bc", "d"], word="abc")
    ic(solution)
