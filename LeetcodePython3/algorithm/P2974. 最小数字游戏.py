#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-22 22:37
FileName: P2974. 最小数字游戏.py
Description:
"""
from typing import List


class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        for i in range(0, len(nums), 2):
            nums[i:i + 2] = nums[i:i + 2][::-1]
        return nums


if __name__ == '__main__':
    solution = Solution().numberGame([5, 4, 2, 3])
    print(solution)
