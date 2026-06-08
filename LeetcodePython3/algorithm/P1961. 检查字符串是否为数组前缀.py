#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-08 22:46
FileName: P1961. 检查字符串是否为数组前缀.py
Description:
"""
from typing import List


class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        ss = ''
        for word in words:
            ss += word
            if ss == s:
                return True
        return False


if __name__ == '__main__':
    solution = Solution().isPrefixString(s="iloveleetcode", words=["i", "love", "leetcode", "apples"])
    print(solution)
