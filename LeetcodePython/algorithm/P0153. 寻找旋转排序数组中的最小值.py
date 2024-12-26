#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-26 23:10
FileName: P0153. 寻找旋转排序数组中的最小值
Description:
"""
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)


if __name__ == '__main__':
    solution = Solution().findMin(nums=[4, 5, 6, 7, 0, 1, 2])
    print(solution)
