#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-10 21:41
FileName: P3280. 将日期转换为二进制表示.py
Description:
"""


class Solution:
    def convertDateToBinary(self, date: str) -> str:
        return '-'.join(bin(int(el))[2:] for el in date.split('-'))


if __name__ == '__main__':
    solution = Solution().convertDateToBinary('1900-1-1')
    print(solution)
