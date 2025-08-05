#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-07-13 18:40
FileName: algorithm/P2294. 划分数组使最大差为 K.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, cnt = nums[0], 1
        for i, num in enumerate(nums):
            if num - left > k:
                cnt += 1
                left = num
        return cnt


if __name__ == '__main__':
    solution = Solution().partitionArray(nums=[3, 6, 1, 2, 5], k=2)
    ic(solution)
