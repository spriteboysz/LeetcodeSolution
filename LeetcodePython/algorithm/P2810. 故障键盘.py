#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-27 21:51
FileName: P2810. 故障键盘
Description:
"""

from icecream import ic


class Solution:
    def finalString(self, s: str) -> str:
        ss = []
        for ch in s:
            if ch == 'i':
                ss = ss[::-1]
            else:
                ss.append(ch)
        return ''.join(ss)


if __name__ == '__main__':
    solution = Solution().finalString(s="string")
    ic(solution)
