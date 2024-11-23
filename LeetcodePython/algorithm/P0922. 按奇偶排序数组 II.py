#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-23 21:24
FileName: P0922. 按奇偶排序数组 II
Description:
"""
from typing import List


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort(key=lambda el: el % 2)
        nums[::2], nums[1::2] = nums[:n // 2], nums[n // 2:]
        return nums


if __name__ == '__main__':
    solution = Solution().sortArrayByParityII(nums=[4, 2, 5, 7])
    print(solution)
