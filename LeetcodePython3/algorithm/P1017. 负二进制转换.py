#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-10 10:31
FileName: algorithm/P1017. 负二进制转换.py
Description: 
"""


class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return '0'
        ss = []
        while n:
            n, mod = divmod(n, -2)
            if mod == -1:
                mod = 1
                n += 1
            ss.append(mod)
        return ''.join(map(str, ss[::-1]))



if __name__ == '__main__':
    solution = Solution().baseNeg2(3)
    print('<None>' if solution is None else f'{solution=}')
