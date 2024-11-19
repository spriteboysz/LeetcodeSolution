#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-19 22:50
FileName: P2520. 统计能整除数字的位数
Description:
"""


class Solution:
    def countDigits(self, num: int) -> int:
        return sum([num % int(i) == 0 for i in list(str(num))])


if __name__ == '__main__':
    solution = Solution().countDigits(1248)
    print(solution)
