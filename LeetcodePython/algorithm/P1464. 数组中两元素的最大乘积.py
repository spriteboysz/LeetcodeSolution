#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-23 21:42
FileName: P1464. 数组中两元素的最大乘积
Description:
"""
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max((nums[0] - 1) * (nums[1] - 1), (nums[-1] - 1) * (nums[-2] - 1))


if __name__ == '__main__':
    solution = Solution().maxProduct([3, 4, 5, 2])
    print(solution)
