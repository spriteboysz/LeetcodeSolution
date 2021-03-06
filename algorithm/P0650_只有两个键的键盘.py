#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-15 22:40
LastEditTime: 2022-06-15 22:40
Description:
FilePath: 650.只有两个键的键盘.py
"""


class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        for i in range(2, n):
            if n % i == 0:
                return self.minSteps(n // i) + i
        return n


if __name__ == '__main__':
    solution = Solution()
    ans = solution.minSteps(3)
    print(ans)
