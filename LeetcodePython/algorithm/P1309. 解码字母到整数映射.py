#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-19 00:06
FileName: P1309. 解码字母到整数映射
Description:
"""

from string import ascii_lowercase


class Solution:
    def freqAlphabets(self, s: str) -> str:
        ss, pos = [], 0
        while pos < len(s):
            if pos + 2 < len(s) and s[pos + 2] == '#':
                ss.append(ascii_lowercase[int(s[pos:pos + 2]) - 1])
                pos += 3
            else:
                ss.append(ascii_lowercase[int(s[pos]) - 1])
                pos += 1
        return ''.join(ss)


if __name__ == '__main__':
    solution = Solution().freqAlphabets(s="1326#")
    print(solution)
