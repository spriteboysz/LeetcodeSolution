#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-01 10:29
FileName: P1752. 检查数组是否经排序和轮转得到
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def check(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                nums = [*nums[i:], *nums[:i]]
                break
        return all(nums[i - 1] <= nums[i] for i in range(1, len(nums)))


if __name__ == '__main__':
    solution = Solution().check(nums=[3, 4, 5, 1, 2])
    ic(solution)
