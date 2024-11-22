#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-22 22:21
FileName: P2894. 分类求和并作差
Description:
"""


class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        sum1, sum2 = 0, 0
        for i in range(1, n + 1):
            if i % m != 0:
                sum1 += i
            else:
                sum2 += i
        return sum1 - sum2


if __name__ == '__main__':
    solution = Solution().differenceOfSums(10, 3)
    print(solution)
