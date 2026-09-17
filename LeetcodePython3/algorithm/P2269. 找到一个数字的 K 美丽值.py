#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-16 14:28
FileName: algorithm/P2269. 找到一个数字的 K 美丽值.py
Description: 
"""


class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        cnt = 0
        ss = str(num)
        for i in range(len(ss) - k + 1):
            sub = int(ss[i:i + k])
            if sub != 0 and num % sub == 0:
                cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().divisorSubstrings(num=240, k=2)
    print('<None>' if solution is None else f'{solution=}')
