#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-22 21:58
FileName: P3264. K 次乘运算后的最终数组 I
Description:
"""
from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            minimum = min(nums)
            for i, num in enumerate(nums):
                if num == minimum:
                    nums[i] = num * multiplier
                    break
        return nums


if __name__ == '__main__':
    solution = Solution().getFinalState(nums=[2, 1, 3, 5, 6], k=5, multiplier=2)
    print(solution)
