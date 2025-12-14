#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-12-14 21:49
FileName: P3745. 三元素表达式的最大值.py
Description:
"""
from typing import List


class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        nums.sort()
        return nums[-1] + nums[-2] - nums[0]


if __name__ == '__main__':
    s = Solution().maximizeExpressionOfThree(nums=[-2, 0, 5, -2, 4])
    print(s)
