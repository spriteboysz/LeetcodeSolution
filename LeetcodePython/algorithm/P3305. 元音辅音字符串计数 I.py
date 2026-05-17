#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-05-03 15:22
FileName: P3305. 元音辅音字符串计数 I.py
Description:
"""


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        cnt = 0
        for i, _ in enumerate(word):
            vowels = set()
            consonants = 0
            for j, ch in enumerate(word[i:], start=i):
                if ch in 'aeiou':
                    vowels.add(ch)
                else:
                    consonants += 1
                if len(vowels) == 5 and consonants == k:
                    cnt += 1
                if consonants > k:
                    break
        return cnt


if __name__ == '__main__':
    solution = Solution().countOfSubstrings(word="iqeaouqi", k=2)
    print(solution)
