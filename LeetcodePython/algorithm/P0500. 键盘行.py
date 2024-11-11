#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-11 22:28
FileName: P0500. 键盘行
Description:
"""
from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keys = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        dic = {ch: i + 1 for i, key in enumerate(keys) for ch in key}
        ans = []
        for word in words:
            if len(set([dic.get(ch.lower()) for ch in word])) == 1:
                ans.append(word)
        return ans


if __name__ == '__main__':
    solution = Solution().findWords(words=["Hello", "Alaska", "Dad", "Peace"])
    print(solution)
