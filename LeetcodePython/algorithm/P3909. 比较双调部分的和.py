#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-05-03 15:09
FileName: P3909. 比较双调部分的和.py
Description:
"""


class Solution:
    def compareBitonicSums(self, nums: list[int]) -> int:
        index = nums.index(max(nums))
        left, right = sum(nums[:index]), sum(nums[index + 1:])
        if left > right:
            return 0
        if left < right:
            return 1
        return -1


if __name__ == '__main__':
    solution = Solution().compareBitonicSums(nums=[1, 3, 2, 1])
    print(solution)
