#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-12 23:31
FileName: P0917. 仅仅反转字母
Description:
"""


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        alphabet = [ch for ch in s if ch.isalpha()]
        ss = []
        for ch in s:
            if ch.isalpha():
                ss.append(alphabet.pop())
            else:
                ss.append(ch)
        return ''.join(ss)


if __name__ == '__main__':
    solution = Solution().reverseOnlyLetters(s="Test1ng-Leet=code-Q!")
    print(solution)
