#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-30 21:59
FileName: P3028. 边界上的蚂蚁
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        acc, cnt = 0, 0
        for num in nums:
            acc += num
            if acc == 0:
                cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().returnToBoundaryCount([2, 3, -5])
    ic(solution)
