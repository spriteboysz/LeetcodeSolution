#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-30 10:44
FileName: LCR 006. 两数之和 II - 输入有序数组
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return [left, right]
        return [-1, -1]


if __name__ == '__main__':
    solution = Solution().twoSum(numbers=[1, 2, 4, 6, 10], target=8)
    ic(solution)
