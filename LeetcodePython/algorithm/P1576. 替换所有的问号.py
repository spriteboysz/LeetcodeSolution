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
            for j in range(ord('a'), ord('z') + 1):
                if chr(j) != ss[i - 1] and chr(j) != ss[i + 1]:
                    ss[i] = chr(j)
                    break
        return ''.join(ss[1:-1])


if __name__ == '__main__':
    solution = Solution().modifyString("?zs?")
    ic(solution)
