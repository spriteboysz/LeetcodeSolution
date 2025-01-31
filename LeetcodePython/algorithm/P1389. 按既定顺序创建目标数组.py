#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-31 22:14
FileName: P1389. 按既定顺序创建目标数组
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        nums2 = []
        for num, i in zip(nums, index):
            nums2.insert(i, num)
        return nums2


if __name__ == '__main__':
    solution = Solution().createTargetArray(nums=[0, 1, 2, 3, 4], index=[0, 1, 2, 2, 1])
    ic(solution)
