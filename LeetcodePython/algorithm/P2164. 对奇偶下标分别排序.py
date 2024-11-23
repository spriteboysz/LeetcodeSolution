#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-23 22:40
FileName: P2164. 对奇偶下标分别排序
Description:
"""
from typing import List


class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        nums[::2] = sorted(nums[::2])
        nums[1::2] = sorted(nums[1::2], reverse=True)
        return nums


if __name__ == '__main__':
    solution = Solution().sortEvenOdd([4,1,2,3])
    print(solution)