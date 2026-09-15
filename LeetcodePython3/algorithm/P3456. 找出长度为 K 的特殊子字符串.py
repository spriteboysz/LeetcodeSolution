#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-14 16:16
FileName: algorithm/P3456. 找出长度为 K 的特殊子字符串.py
Description: 
"""


class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        ss, counts = [s[0]], [1]
        for c in s[1:]:
            if c == ss[-1]:
                counts[-1] += 1
            else:
                ss.append(c)
                counts.append(1)
        return k in counts


if __name__ == '__main__':
    solution = Solution().hasSpecialSubstring('aaabaaa', 3)
    print('<None>' if solution is None else f'{solution=}')
