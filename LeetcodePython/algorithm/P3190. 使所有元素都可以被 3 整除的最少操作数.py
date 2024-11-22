#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-21 23:07
FileName: P3190. 使所有元素都可以被 3 整除的最少操作数
Description:
"""
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return sum([num % 3 != 0 for num in nums])


if __name__ == '__main__':
    solution = Solution().minimumOperations(nums=[1, 2, 3, 4])
    print(solution)
