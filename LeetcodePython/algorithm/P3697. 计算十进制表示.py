#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-10-12 11:57
FileName: P3697. 计算十进制表示.py
Description:
"""
from typing import List


class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        return [int(digit) * 10 ** i for i, digit in enumerate(str(n)[::-1]) if digit != '0'][::-1]


if __name__ == '__main__':
    s = Solution().decimalRepresentation(n=537)
    print(s)
