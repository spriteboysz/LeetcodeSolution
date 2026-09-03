#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-03 14:13
FileName: LC/LCR 006. 两数之和 II - 输入有序数组.py
Description: 
"""
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left, right]
            if numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
        return [-1, -1]


if __name__ == '__main__':
    solution = Solution().twoSum([1, 2, 4, 6, 10], target=8)
    print(solution)
