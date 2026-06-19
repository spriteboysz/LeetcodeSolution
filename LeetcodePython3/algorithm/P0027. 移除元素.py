#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-19 22:12
FileName: P0027. 移除元素.py
Description:
"""
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        print(nums)
        return k


if __name__ == '__main__':
    solution = Solution().removeElement([2, 3, 2, 3], val=3)
    print(solution)
