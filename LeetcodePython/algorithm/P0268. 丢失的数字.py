#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-10 23:08
FileName: P0268. 丢失的数字
Description:
"""
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return (n + 1) * n // 2 - sum(nums)


if __name__ == '__main__':
    solution = Solution().missingNumber([3, 0, 1])
    print(solution)
