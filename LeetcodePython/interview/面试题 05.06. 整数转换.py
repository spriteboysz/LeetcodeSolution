#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-22 19:53
FileName: 面试题 05.06. 整数转换
Description:
"""
from itertools import zip_longest


class Solution:
    def convertInteger(self, num1: int, num2: int) -> int:
        if num1 < 0:
            num1 += (1 << 32)
        if num2 < 0:
            num2 += (1 << 32)

        s1, s2 = bin(num1)[2:][::-1], bin(num2)[2:][::-1]
        cnt = 0
        for ch1, ch2 in zip_longest(s1, s2, fillvalue='0'):
            if ch1 != ch2:
                cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().convertInteger(29, -15)
    print(solution)
