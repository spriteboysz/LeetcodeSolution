#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-26 16:43
FileName: algorithm/P0809. 情感丰富的文字.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        cnt = 0
        for word in words:
            i, j = 0, 0
            counter = 1
            while i < len(s):
                if j < len(word) and s[i] == word[j]:
                    if counter == 2:
                        if word[j - 1] != word[j - 2]:
                            break
                    counter = 1
                    i += 1
                    j += 1
                elif j > 0 and s[i] == word[j - 1]:
                    i += 1
                    counter += 1
                else:
                    break
            if i == len(s) and j == len(word):
                if counter == 2 and word[j - 1] != word[j - 2]:
                    continue
                cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().expressiveWords(s="heeellooo", words=["hello", "hi", "helo"])
    ic(solution)
