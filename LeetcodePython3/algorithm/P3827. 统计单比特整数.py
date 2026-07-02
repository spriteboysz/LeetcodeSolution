#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-30 23:03
FileName: P3827. 统计单比特整数.py
Description:
"""


class Solution:
    def countMonobit(self, n: int) -> int:
        cnt = 0
        while 2 ** cnt - 1 <= n:
            cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().countMonobit(4)
    print(solution)
