#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-14 18:56
FileName: P1470. 重新排列数组.py
Description:
"""
from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums[::2], nums[1::2] = nums[:n], nums[n:]
        return nums


if __name__ == '__main__':
    solution = Solution().shuffle(nums=[2, 5, 1, 3, 4, 7], n=3)
    print(solution)
