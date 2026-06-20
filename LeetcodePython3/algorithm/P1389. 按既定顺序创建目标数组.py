#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-20 10:33
FileName: P1389. 按既定顺序创建目标数组.py
Description:
"""
from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for num, i in zip(nums, index):
            target.insert(i, num)
        return target


if __name__ == '__main__':
    solution = Solution().createTargetArray(nums = [0,1,2,3,4], index = [0,1,2,2,1])
    print(solution)
