#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-04 14:02
FileName: P0396. 旋转函数.py
Description:
"""
from typing import List


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        return max(sum(j * num for j, num in enumerate(nums[i:] + nums[:i])) for i in range(len(nums)))


if __name__ == '__main__':
    solution = Solution().maxRotateFunction(nums=[4, 3, 2, 6])
    print(solution)
