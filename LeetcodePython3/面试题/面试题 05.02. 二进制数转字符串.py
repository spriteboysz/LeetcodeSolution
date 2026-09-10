#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-09 11:16
FileName: 面试题/面试题 05.02. 二进制数转字符串.py
Description: 
"""
import doctest


class Solution:
    def printBin(self, num: float) -> str:
        """
        >>> Solution().printBin(0.625)
        '0.101'
        """
        ss = []
        while num:
            div, num = divmod(num * 2, 1)
            ss.append(int(div))
            if len(ss) > 30:
                return 'Error'
        return '0.' + ''.join(map(str, ss))


if __name__ == '__main__':
    solution = Solution().printBin(0.125)
    print('<None>' if not solution else f'{solution=}')
    doctest.testmod()
