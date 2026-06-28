#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-28 11:08
FileName: P2180. 统计各位数字之和为偶数的整数个数.py
Description:
"""


class Solution:
    def countEven(self, num: int) -> int:
        return sum(sum(int(digit) for digit in str(i)) % 2 == 0 for i in range(2, num + 1))


if __name__ == '__main__':
    solution = Solution().countEven(30)
    print(solution)
