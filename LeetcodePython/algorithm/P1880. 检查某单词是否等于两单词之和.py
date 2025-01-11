#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-10 22:58
FileName: P1880. 检查某单词是否等于两单词之和
Description:
"""

from icecream import ic


class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def process(s):
            num = 0
            for ch in s:
                num = num * 10 + ord(ch) - ord('a')
            return num

        return process(firstWord) + process(secondWord) == process(targetWord)


if __name__ == '__main__':
    solution = Solution().isSumEqual(firstWord="aaa", secondWord="a", targetWord="aaaa")
    ic(solution)
