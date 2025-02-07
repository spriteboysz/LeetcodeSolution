#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-07 21:50
FileName: P2670. 找出不同元素数目差数组
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        return [len(set(nums[:i + 1])) - len(set(nums[i + 1:])) for i in range(len(nums))]


if __name__ == '__main__':
    solution = Solution().distinctDifferenceArray([1, 2, 3, 4, 5])
    ic(solution)
