#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-30 10:40
FileName: 面试题 16.05. 阶乘尾数
Description:
"""

from icecream import ic


class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0
        count = 0
        while n > 0:
            n //= 5
            count += n
        return count


if __name__ == '__main__':
    solution = Solution().trailingZeroes(6)
    ic(solution)
