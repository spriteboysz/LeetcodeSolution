#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-17 23:01
FileName: P0561. 数组拆分
Description:
"""
from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums, reverse=True)[1::2])


if __name__ == '__main__':
    solution = Solution().arrayPairSum([6, 2, 6, 5, 1, 2])
    print(solution)
