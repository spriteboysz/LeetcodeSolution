#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-17 23:06
FileName: P2785. 将字符串中的元音字母排序
Description:
"""

from icecream import ic


class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
        vowel = [ch for ch in s if ch in vowels]
        vowel.sort(reverse=True)
        ss = []
        for ch in s:
            if ch in vowels:
                ss.append(vowel.pop())
            else:
                ss.append(ch)
        return ''.join(ss)


if __name__ == '__main__':
    solution = Solution().sortVowels(s="lEetcOde")
    ic(solution)
