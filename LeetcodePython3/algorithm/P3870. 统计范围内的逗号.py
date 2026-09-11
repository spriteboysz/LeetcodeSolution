#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-10 15:26
FileName: algorithm/P3870. 统计范围内的逗号.py
Description: 
"""


class Solution:
    def countCommas(self, n: int) -> int:
        cnt, left = 0, 1000
        while left <= n:
            cnt += n - left + 1
            left *= 1000
        return cnt


if __name__ == '__main__':
    solution = Solution().countCommas(1002)
    print('<None>' if solution is None else f'{solution=}')
