#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-13 13:43
FileName: P2047. 句子中的有效单词数.py
Description:
"""
import re


class Solution:
    def countValidWords(self, sentence: str) -> int:
        pattern = re.compile(r'^([,.!]|[a-z]+(-[a-z]+)?[,.!]?)$')
        return sum(bool(pattern.match(word)) for word in sentence.split())


if __name__ == '__main__':
    solution = Solution().countValidWords(sentence="!this  1-s b8d! w")
    print(solution)
