#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-09 08:46
FileName: 面试题/面试题 10.05. 稀疏数组搜索.py
Description: 
"""
from typing import List


class Solution:
    def findString(self, words: List[str], s: str) -> int:
        for i, word in enumerate(words):
            if word == s:
                return i
        return -1


if __name__ == '__main__':
    solution = Solution().findString(words=["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""], s="ta")
    print('<None>' if not solution else f'{solution=}')
