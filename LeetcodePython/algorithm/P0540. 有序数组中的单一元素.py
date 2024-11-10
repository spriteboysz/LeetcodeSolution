#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-10 23:24
FileName: P0540. 有序数组中的单一元素
Description:
"""
from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        single = 0
        for num in nums:
            single ^= num
        return single


if __name__ == '__main__':
    solution = Solution().singleNonDuplicate(nums=[1, 1, 2, 3, 3, 4, 4, 8, 8])
    print(solution)
