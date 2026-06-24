#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-23 22:55
FileName: P2562. 找出数组的串联值.py
Description:
"""
from typing import List


class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        conc = 0
        for i in range(len(nums) // 2):
            conc += int(str(nums[i]) + str(nums[-i - 1]))
        if len(nums) % 2 == 1:
            conc += nums[len(nums) // 2]
        return conc


if __name__ == '__main__':
    solution = Solution().findTheArrayConcVal(nums=[5, 14, 13, 8, 12])
    print(solution)
