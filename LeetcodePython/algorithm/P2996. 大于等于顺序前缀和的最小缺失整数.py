#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-24 12:28
FileName: P2996. 大于等于顺序前缀和的最小缺失整数
Description:
"""
from typing import List


class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        total = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                total += nums[i]
            else:
                break
        seen = set(nums)
        while total in seen:
            total += 1
        return total


if __name__ == '__main__':
    solution = Solution().missingInteger(nums=[3, 4, 5, 1, 12, 14, 13])
    print(solution)
