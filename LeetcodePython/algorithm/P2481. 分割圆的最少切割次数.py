#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-18 23:25
FileName: P2481. 分割圆的最少切割次数
Description:
"""


class Solution:
    def numberOfCuts(self, n: int) -> int:
        if n == 1:
            return 0
        return n if n % 2 == 1 else n // 2


if __name__ == '__main__':
    solution = Solution().numberOfCuts(7)
    print(solution)
