#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-15 19:41
FileName: P0724. 寻找数组的中心下标
Description:
"""
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total, acc = sum(nums), 0
        for i, num in enumerate(nums):
            total -= num
            if acc == total:
                return i
            acc += num
        return -1


if __name__ == '__main__':
    solution = Solution().pivotIndex(nums=[1, 7, 3, 6, 5, 6])
    print(solution)
