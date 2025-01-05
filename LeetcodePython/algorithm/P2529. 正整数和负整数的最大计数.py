#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-05 11:44
FileName: P2529. 正整数和负整数的最大计数
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        cnt1, cnt2 = 0, 0
        for num in nums:
            if num < 0:
                cnt1 += 1
            if num > 0:
                cnt2 += 1
        return max(cnt1, cnt2)


if __name__ == '__main__':
    solution = Solution().maximumCount(nums=[-2, -1, -1, 1, 2, 3])
    ic(solution)
