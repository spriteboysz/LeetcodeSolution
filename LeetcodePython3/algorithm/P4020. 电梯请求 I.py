#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-31 22:37
FileName: algorithm/P4020. 电梯请求 I.py
Description: 
"""
from itertools import pairwise


class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        print(n)
        return sum(abs(b - a) for a, b in pairwise(requests)) + requests[0]


if __name__ == '__main__':
    solution = Solution().elevatorRequests(n=5, requests=[2, 1, 4, 3])
    print(solution)
