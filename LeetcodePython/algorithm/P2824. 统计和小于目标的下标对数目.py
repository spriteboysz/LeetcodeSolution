#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-06 23:21
FileName: P2824. 统计和小于目标的下标对数目
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        cnt = 0
        for j, num2 in enumerate(nums):
            for num1 in nums[:j]:
                if num1 + num2 < target:
                    cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().countPairs(nums=[-1, 1, 2, 3, 1], target=2)
    ic(solution)
