#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-19 23:13
FileName: P2652. 倍数求和
Description:
"""


class Solution:
    def sumOfMultiples(self, n: int) -> int:
        return sum([num for num in range(3, n + 1) if num % 3 == 0 or num % 5 == 0 or num % 7 == 0])


if __name__ == '__main__':
    solution = Solution().sumOfMultiples(7)
    print(solution)
