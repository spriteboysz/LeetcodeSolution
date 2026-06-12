#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-12 22:23
FileName: P2273. 移除字母异位词后的结果数组.py
Description:
"""
from typing import List


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        alphabets = []
        for word in words:
            alphabet = [0] * 26
            for ch in word:
                alphabet[ord(ch) - ord('a')] += 1
            alphabets.append(alphabet)

        stack1, stack2 = [], []
        for word, alphabet in zip(words, alphabets):
            if not stack2 or stack2[-1] != alphabet:
                stack1.append(word)
                stack2.append(alphabet)
        return stack1


if __name__ == '__main__':
    solution = Solution().removeAnagrams(words=["abba", "baba", "bbaa", "cd", "cd"])
    print(solution)
