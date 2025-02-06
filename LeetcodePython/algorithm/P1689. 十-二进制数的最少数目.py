#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-03 22:43
FileName: P1689. 十-二进制数的最少数目
Description:
"""

from icecream import ic


class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(n))


if __name__ == '__main__':
    solution = Solution().minPartitions(n="82734")
    ic(solution)
