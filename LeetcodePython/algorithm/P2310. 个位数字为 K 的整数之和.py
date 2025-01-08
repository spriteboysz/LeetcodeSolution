#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-07 23:45
FileName: P2310. 个位数字为 K 的整数之和
Description:
"""

from icecream import ic


class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0:
            return 0
        for i in range(1, num + 1):
            if num - i * k < 0:
                break
            if (num - i * k) % 10 == 0:
                return i
        return -1


if __name__ == '__main__':
    solution = Solution().minimumNumbers(58, 9)
    ic(solution)
