#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-05-31 15:53
FileName: P3819. 非负元素轮替.py
Description:
"""
from typing import List


class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        positive = [num for num in nums if num >= 0]
        if len(positive) == 0:
            return nums
        k %= len(positive)
        positive = positive[k:] + positive[:k]
        pos = 0
        for i, num in enumerate(nums):
            if num >= 0:
                nums[i] = positive[pos]
                pos += 1
        return nums


if __name__ == '__main__':
    solution = Solution().rotateElements(nums=[1, -2, 3, -4], k=3)
    print(solution)
