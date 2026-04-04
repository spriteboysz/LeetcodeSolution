#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-04-04 21:27
FileName: P3870. 统计范围内的逗号.py
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
    solution = Solution().countCommas(n=1002)
    print(solution)
