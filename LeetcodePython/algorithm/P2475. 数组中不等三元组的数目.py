#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-02 11:38
FileName: P2475. 数组中不等三元组的数目
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        cnt = 0
        for k, num3 in enumerate(nums):
            for j, num2 in enumerate(nums[:k]):
                for _, num1 in enumerate(nums[:j]):
                    if num1 != num2 and num1 != num3 and num2 != num3:
                        cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().unequalTriplets(nums=[4, 4, 2, 4, 3])
    ic(solution)
