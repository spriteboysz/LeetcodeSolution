#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-19 21:26
FileName: P0167. 两数之和 II - 输入有序数组.py
Description:
"""
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, num in enumerate(numbers):
            left, right = i + 1, len(numbers) - 1
            while left <= right:
                mid = (left + right) // 2
                if numbers[mid] == target - num:
                    return [i + 1, mid + 1]
                if numbers[mid] > target - num:
                    right = mid - 1
                else:
                    left = mid + 1
        return [-1, -1]


if __name__ == '__main__':
    solution = Solution().twoSum(numbers=[2, 7, 11, 15], target=9)
    print(solution)
