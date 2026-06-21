#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-20 21:42
FileName: P3697. 计算十进制表示.py
Description:
"""
from typing import List


class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        nums, k = [], 0
        while n > 0:
            n, mod = divmod(n, 10)
            if mod != 0:
                nums.append(mod * 10 ** k)
            k += 1
        return nums[::-1]


if __name__ == '__main__':
    solution = Solution().decimalRepresentation(507)
    print(solution)
