#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-16 18:11
FileName: P2549. 统计桌面上的不同数字
Description:
"""


class Solution:
    def distinctIntegers(self, n: int) -> int:
        return 1 if n == 1 else n - 1


if __name__ == '__main__':
    solution = Solution().distinctIntegers(100)
    print(solution)
