#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-26 11:12
FileName: P3330. 找到初始输入字符串 I.py
Description:
"""


class Solution:
    def possibleStringCount(self, word: str) -> int:
        cnt = 1
        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().possibleStringCount('abbcccc')
    print(solution)
