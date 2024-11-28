#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-22 23:15
FileName: P905. 按奇偶排序数组
Description:
"""
from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return sorted(nums, key=lambda el: el % 2)


if __name__ == '__main__':
    solution = Solution().sortArrayByParity(nums=[3, 1, 2, 4])
    print(solution)
