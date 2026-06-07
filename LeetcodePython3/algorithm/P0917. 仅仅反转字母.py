#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-07 10:50
FileName: P0917. 仅仅反转字母.py
Description:
"""


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        letters = [ch for ch in s if ch.isalpha()]
        ss = list(s)
        for i, ch in enumerate(ss):
            if ch.isalpha():
                ss[i] = letters.pop()
        return ''.join(ss)


if __name__ == '__main__':
    solution = Solution().reverseOnlyLetters(s="a-bC-dEf-ghIj")
    print(solution)
