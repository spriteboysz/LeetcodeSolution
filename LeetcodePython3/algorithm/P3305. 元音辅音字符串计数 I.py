#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-15 11:09
FileName: algorithm/P3305. 元音辅音字符串计数 I.py
Description: 
"""


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        cnt = 0
        for i in range(len(word)):
            vowels, consonants = set(), 0
            for ch in word[i:]:
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
    solution = Solution().countOfSubstrings(word="ieaouqqieaouqq", k=1)
    print(solution)
