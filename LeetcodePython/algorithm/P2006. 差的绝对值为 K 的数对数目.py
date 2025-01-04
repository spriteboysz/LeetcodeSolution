#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-04 21:17
FileName: P2006. 差的绝对值为 K 的数对数目
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        cnt = 0
        for i, num1 in enumerate(nums):
            for num2 in nums[:i]:
                if abs(num1 - num2) == k:
                    cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().countKDifference(nums=[1, 2, 2, 1], k=1)
    ic(solution)
