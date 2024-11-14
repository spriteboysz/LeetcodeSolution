#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-14 23:47
FileName: P0628. 三个数的最大乘积
Description:
"""
from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        return max(nums[0] * nums[1] * nums[2], nums[0] * nums[-2] * nums[-1])


if __name__ == '__main__':
    solution = Solution().maximumProduct([1, 2, 3])
    print(solution)
