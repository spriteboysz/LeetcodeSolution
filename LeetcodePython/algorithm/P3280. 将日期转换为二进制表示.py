#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-21 23:16
FileName: P3280. 将日期转换为二进制表示
Description:
"""


class Solution:
    def convertDateToBinary(self, date: str) -> str:
        return '-'.join(map(lambda el: bin(int(el))[2:], date.split('-')))


if __name__ == '__main__':
    solution = Solution().convertDateToBinary(date="2080-02-29")
    print(solution)
