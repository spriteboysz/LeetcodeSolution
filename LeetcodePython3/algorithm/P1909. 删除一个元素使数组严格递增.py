#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-23 23:09
FileName: P1909. 删除一个元素使数组严格递增.py
Description:
"""
from itertools import pairwise
from typing import List


class Solution:
    @staticmethod
    def check(nums: List[int]):
        return all(num1 < num2 for num1, num2 in pairwise(nums))

    def canBeIncreasing(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]:
                return self.check(nums[:i - 1] + nums[i:]) or self.check(nums[:i] + nums[i + 1:])
        return True


if __name__ == '__main__':
    solution = Solution().canBeIncreasing(nums=[1, 2, 10, 5, 7])
    print(solution)
