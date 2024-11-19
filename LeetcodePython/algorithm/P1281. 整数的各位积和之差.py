#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-18 23:03
FileName: P1281. 整数的各位积和之差
Description:
"""
from functools import reduce


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        nums = list(map(int, list(str(n))))
        return reduce(lambda a, b: a * b, nums) - sum(nums)


if __name__ == '__main__':
    solution = Solution().subtractProductAndSum(234)
    print(solution)
