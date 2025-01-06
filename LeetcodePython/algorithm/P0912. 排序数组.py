#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-06 23:22
FileName: P0912. 排序数组
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return sorted(nums)


if __name__ == '__main__':
    solution = Solution().sortArray([5, 1, 1, 2, 0, 0])
    ic(solution)
