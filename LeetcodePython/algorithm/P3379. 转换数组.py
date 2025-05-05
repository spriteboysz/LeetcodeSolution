#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-05-05 11:40
FileName: algorithm/P3379. 转换数组.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        return [nums[(i + num) % len(nums)] for i, num in enumerate(nums)]


if __name__ == '__main__':
    solution = Solution().constructTransformedArray(nums=[3, -2, 1, 1])
    ic(solution)
