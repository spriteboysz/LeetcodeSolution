#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-31 22:36
FileName: P1576. 替换所有的问号
Description:
"""

from icecream import ic


class Solution:
    def modifyString(self, s: str) -> str:
        ss = ['*', *list(s), '*']
        for i, ch in enumerate(f'*{s}*'):
            if ch != '?':
                continue
            for j in range(26):
                ch2 = chr(j + ord('a'))
                if ch2 != ss[i - 1] and ch2 != ss[i + 1]:
                    ss[i] = ch2
                    break
        return ''.join(ss[1:-1])


if __name__ == '__main__':
    solution = Solution().modifyString("?zs?")
    ic(solution)
