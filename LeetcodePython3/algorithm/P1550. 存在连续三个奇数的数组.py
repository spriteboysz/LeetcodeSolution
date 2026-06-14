#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-14 21:15
FileName: P1550. 存在连续三个奇数的数组.py
Description:
"""
from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        nums = [num % 2 for num in arr]
        return any(sum(nums[i:i + 3]) == 3 for i in range(0, len(nums) - 2))


if __name__ == '__main__':
    solution = Solution().threeConsecutiveOdds(arr=[1, 2, 34, 3, 4, 5, 7, 24, 12])
    print(solution)
