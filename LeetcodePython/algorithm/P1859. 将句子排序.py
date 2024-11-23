#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-23 22:23
FileName: P1859. 将句子排序
Description:
"""


class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        return ' '.join(map(lambda el: el[:-1], sorted(words, key=lambda word: word[-1])))


if __name__ == '__main__':
    solution = Solution().sortSentence(s="is2 sentence4 This1 a3")
    print(solution)
