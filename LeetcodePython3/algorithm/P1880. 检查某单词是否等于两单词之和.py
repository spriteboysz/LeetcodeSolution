#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-13 13:40
FileName: P1880. 检查某单词是否等于两单词之和.py
Description:
"""


class Solution:
    @staticmethod
    def calc(s):
        return int(''.join(str(ord(ch) - ord('a')) for ch in s))

    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        return self.calc(firstWord) + self.calc(secondWord) == self.calc(targetWord)


if __name__ == '__main__':
    solution = Solution().isSumEqual(firstWord="acb", secondWord="cba", targetWord="cdb")
    print(solution)
