#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-17 22:09
FileName: P2413. 最小偶倍数
Description:
"""


class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n if n % 2 == 0 else n * 2


if __name__ == '__main__':
    solution = Solution().smallestEvenMultiple(6)
    print(solution)
