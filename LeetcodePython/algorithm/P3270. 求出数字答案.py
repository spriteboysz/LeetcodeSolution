#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-21 22:51
FileName: P3270. 求出数字答案
Description:
"""
from itertools import zip_longest


class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        s1, s2, s3 = map(lambda el: str(el)[::-1], [num1, num2, num3])
        ss = [min(a, b, c) for a, b, c in zip_longest(s1, s2, s3, fillvalue='0')]
        return int(''.join(ss)[::-1])


if __name__ == '__main__':
    solution = Solution().generateKey(num1=1, num2=10, num3=1000)
    print(solution)
