#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-28 12:20
FileName: P2729. 判断一个数是否迷人.py
Description:
"""


class Solution:
    def isFascinating(self, n: int) -> bool:
        ss = str(n) + str(n * 2) + str(n * 3)
        return len(ss) == 9 and set(ss) == set(map(str, range(1, 10)))


if __name__ == '__main__':
    solution = Solution().isFascinating(783)
    print(solution)
