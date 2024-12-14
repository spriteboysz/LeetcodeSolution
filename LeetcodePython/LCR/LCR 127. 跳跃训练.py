#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-14 19:30
FileName: LCR 127. 跳跃训练
Description:
"""


class Solution:
    def trainWays(self, num: int) -> int:
        if num <= 2:
            return max(1, num)
        a, b = 1, 2
        for _ in range(num - 2):
            a, b = b, a + b
        return b % (10 ** 9 + 7)


if __name__ == '__main__':
    solution = Solution().trainWays(5)
    print(solution)
