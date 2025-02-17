#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-17 23:01
FileName: P2740. 找出分区值
Description:
"""
from itertools import pairwise
from typing import List

from icecream import ic


class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        return min(y - x for x, y in pairwise(nums))


if __name__ == '__main__':
    solution = Solution().findValueOfPartition(nums=[1, 3, 2, 4])
    ic(solution)
