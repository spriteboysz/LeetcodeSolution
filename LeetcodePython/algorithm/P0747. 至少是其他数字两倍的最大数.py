#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-23 21:00
FileName: P0747. 至少是其他数字两倍的最大数
Description:
"""
from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        nums = [(num, i) for i, num in enumerate(nums)]
        nums.sort(key=lambda el: el[0], reverse=True)
        if nums[0][0] >= nums[1][0] * 2:
            return nums[0][1]
        return -1


if __name__ == '__main__':
    solution = Solution().dominantIndex(nums=[3, 6, 1, 0])
    print(solution)
