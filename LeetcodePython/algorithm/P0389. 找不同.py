#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-11 22:06
FileName: P0389. 找不同
Description:
"""


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        alphabet = [0] * 26
        for ch1, ch2 in zip(s, t):
            alphabet[ord(ch1) - ord('a')] -= 1
            alphabet[ord(ch2) - ord('a')] += 1
        alphabet[ord(t[-1]) - ord('a')] += 1
        for i, num in enumerate(alphabet):
            if num == 1:
                return chr(i + ord('a'))
        return 'error'


if __name__ == '__main__':
    solution = Solution().findTheDifference(s="abcd", t="abcde")
    print(solution)
