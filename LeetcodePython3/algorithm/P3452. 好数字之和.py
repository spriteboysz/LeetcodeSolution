#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-08 11:42
FileName: P3452. 好数字之和.py
Description:
"""
from typing import List


class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        cnt = 0
        n = len(nums)
        for i, num in enumerate(nums):
            if (i - k < 0 or num > nums[i - k]) and (i + k >= n or num > nums[i + k]):
                cnt += num
        return cnt


if __name__ == '__main__':
    solution = Solution().sumOfGoodNumbers(nums=[1, 3, 2, 1, 5, 4], k=2)
    print(solution)
