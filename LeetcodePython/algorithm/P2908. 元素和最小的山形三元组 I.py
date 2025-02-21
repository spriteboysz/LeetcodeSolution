#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-02 23:20
FileName: P2908. 元素和最小的山形三元组 I
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        score = []
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums[i:], i):
                for k, num3 in enumerate(nums[j:]):
                    if num2 > num1 and num2 > num3:
                        score.append(num1 + num2 + num3)
        return min(score) if score else -1


if __name__ == '__main__':
    solution = Solution().minimumSum(nums=[8, 6, 1, 5, 3])
    ic(solution)
