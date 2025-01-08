#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-08 23:20
FileName: P1470. 重新排列数组
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums[::2], nums[1::2] = nums[:n], nums[n:]
        return nums
        # return sum([[a, b] for a, b in zip(nums[:n], nums[n:])], [])


if __name__ == '__main__':
    solution = Solution().shuffle(nums=[1, 2, 3, 4, 4, 3, 2, 1], n=4)
    ic(solution)
