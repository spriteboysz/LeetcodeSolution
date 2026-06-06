#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-06 12:37
FileName: P0013. 罗马数字转整数.py
Description:
"""
from collections import OrderedDict
from itertools import pairwise


class Solution:
    def romanToInt(self, s: str) -> int:
        dic = OrderedDict({
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        })
        num = 0
        for ch1, ch2 in pairwise(s):
            num1, num2 = dic.get(ch1, 0), dic.get(ch2, 0)
            if num1 >= num2:
                num += num1
            else:
                num -= num1
        return num + dic.get(s[-1])


if __name__ == '__main__':
    solution = Solution().romanToInt('III')
    print(solution)
