#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-15 20:18
FileName: P0476. 数字的补数
Description:
"""


class Solution:
    def findComplement(self, num: int) -> int:
        return int(''.join(map(str, [1 - int(ch) for ch in bin(num)[2:]])), 2)


if __name__ == '__main__':
    solution = Solution().findComplement(5)
    print(solution)
