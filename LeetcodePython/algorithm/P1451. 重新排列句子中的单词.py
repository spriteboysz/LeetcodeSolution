#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-12 10:33
FileName: algorithm/P1451. 重新排列句子中的单词.py
Description: 
"""

from icecream import ic


class Solution:
    def arrangeWords(self, text: str) -> str:
        return ' '.join(sorted(text.lower().split(), key=len)).capitalize()


if __name__ == '__main__':
    solution = Solution().arrangeWords(text = "Keep calm and code on")
    ic(solution)
