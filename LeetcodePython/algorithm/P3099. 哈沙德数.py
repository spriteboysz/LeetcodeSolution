#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-22 22:10
FileName: P3099. 哈沙德数
Description:
"""


class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        if x % (total := sum(map(int, str(x)))) == 0:
            return total
        return -1


if __name__ == '__main__':
    solution = Solution().sumOfTheDigitsOfHarshadNumber(18)
    print(solution)
