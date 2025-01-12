#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-12 14:01
FileName: P1961. 检查字符串是否为数组前缀
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        ss = ''
        for word in words:
            ss += word
            if len(ss) == len(s):
                return ss == s
            elif len(ss) > len(s):
                break
        return False


if __name__ == '__main__':
    solution = Solution().isPrefixString(s="iloveleetcode", words=["i", "love", "leetcode", "apples"])
    ic(solution)
