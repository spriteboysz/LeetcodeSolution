#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-19 23:24
FileName: P2729. 判断一个数是否迷人
Description:
"""

from string import digits


class Solution:
    def isFascinating(self, n: int) -> bool:
        ss = str(n) + str(n * 2) + str(n * 3)
        return len(ss) == 9 and set(list(ss)) == set(list(digits)) - {'0'}


if __name__ == '__main__':
    solution = Solution().isFascinating(783)
    print(solution)
