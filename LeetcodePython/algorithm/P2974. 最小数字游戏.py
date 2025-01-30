#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-30 22:11
FileName: P2974. 最小数字游戏
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        nums[::2], nums[1::2] = nums[1::2], nums[::2]
        return nums


if __name__ == '__main__':
    solution = Solution().numberGame([5, 4, 2, 3])
    ic(solution)
