#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-11 22:14
FileName: P0345. 反转字符串中的元音字母
Description:
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        vowels = [ch for ch in s if ch in vowel]
        ss = []
        for ch in s:
            if ch in vowel:
                ss.append(vowels.pop())
            else:
                ss.append(ch)
        return ''.join(ss)


if __name__ == '__main__':
    solution = Solution().reverseVowels(s="IceCreAm")
    print(solution)
