#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-06-22 11:19
FileName: algorithm/P3582. 为视频标题生成标签.py
Description: 
"""

from icecream import ic


class Solution:
    def generateTag(self, caption: str) -> str:
        words = ''.join(ch for ch in caption if ch.isalpha() or ch == ' ').split()
        return '#' + ''.join(word.capitalize() if i > 0 else word.lower() for i, word in enumerate(words))[:99]



if __name__ == '__main__':
    solution = Solution().generateTag(caption="Leetcode daily streak achieved")
    ic(solution)
