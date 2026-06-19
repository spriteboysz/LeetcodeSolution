#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-19 11:37
FileName: P1370. 上升下降字符串.py
Description:
"""


class Solution:
    def sortString(self, s: str) -> str:
        alphabet = [0] * 26
        for ch in s:
            alphabet[ord(ch) - ord('a')] += 1
        ss = []
        while sum(alphabet) > 0:
            for i in range(26):
                if alphabet[i] > 0:
                    ss.append(chr(ord('a') + i))
                    alphabet[i] -= 1
            for i in range(25, -1, -1):
                if alphabet[i] > 0:
                    ss.append(chr(ord('a') + i))
                    alphabet[i] -= 1
        return ''.join(ss)


if __name__ == '__main__':
    solution = Solution().sortString(s="aaaabbbbcccc")
    print(solution)
