#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-01 22:12
FileName: P0868. 二进制间距
Description:
"""


class Solution:
    def binaryGap(self, n: int) -> int:
        if n.bit_count() == 1:
            return 0
        return max(map(len, bin(n)[2:].rstrip('0').split('1'))) + 1


if __name__ == '__main__':
    solution = Solution().binaryGap(6)
    print(solution)
