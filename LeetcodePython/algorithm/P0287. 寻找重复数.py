#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-05 16:11
FileName: P0287. 寻找重复数
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            abs_num = abs(num)
            if nums[abs_num - 1] < 0:
                return abs_num
            nums[abs_num - 1] *= -1
        return -1


if __name__ == '__main__':
    solution = Solution().findDuplicate(nums=[1, 3, 4, 2, 2])
    ic(solution)
