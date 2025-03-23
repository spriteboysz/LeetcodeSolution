#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-23 10:47
FileName: algorithm/P3192. 使二进制数组全部等于 1 的最少操作次数 II.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = 0
        for num in nums:
            num ^= cnt & 1
            cnt += 1 - num
        return cnt


if __name__ == '__main__':
    solution = Solution().minOperations(nums=[0, 1, 1, 0, 1])
    ic(solution)
