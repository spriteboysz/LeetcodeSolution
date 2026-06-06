#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-06 20:25
FileName: P0500. 键盘行.py
Description:
"""
from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keyboards = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        dic = {ch: i for i, row in enumerate(keyboards) for ch in row}
        return [word for word in words if len(set(dic.get(ch.lower()) for ch in word)) == 1]


if __name__ == '__main__':
    solution = Solution().findWords(words=["Hello", "Alaska", "Dad", "Peace"])
    print(solution)
