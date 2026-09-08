#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-07 15:25
FileName: 面试题/面试题 05.07. 配对交换.py
Description: 
"""


class Solution:
    def exchangeBits(self, num: int) -> int:
        ss = list(bin(num)[2:].zfill(32))
        ss[::2], ss[1::2] = ss[1::2], ss[::2]
        return int(''.join(ss), 2)


if __name__ == '__main__':
    solution = Solution().exchangeBits(2)
    print('<None>' if not solution else f'{solution=}')
