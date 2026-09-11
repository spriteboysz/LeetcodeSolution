#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-10 11:10
FileName: algorithm/P1404. 将二进制表示减到 1 的步骤数.py
Description: 
"""


class Solution:
    def numSteps(self, s: str) -> int:
        num = int(s, 2)
        cnt = 0
        while num > 1:
            if num % 2 == 0:
                num //= 2
            else:
                num += 1
            cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().numSteps('1101')
    print('<None>' if solution is None else f'{solution=}')
