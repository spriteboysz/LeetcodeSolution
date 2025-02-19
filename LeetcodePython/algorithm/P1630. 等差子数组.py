#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-18 23:16
FileName: P1630. 等差子数组
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def check(left, right):
            sub = sorted(nums[left:right + 1])
            diff = sub[1] - sub[0]
            for j in range(1, len(sub)):
                if sub[j] - sub[j - 1] != diff:
                    return False
            return True

        return [check(a, b) for a, b in zip(l, r)]


if __name__ == '__main__':
    solution = Solution().checkArithmeticSubarrays(nums=[4, 6, 5, 9, 3, 7], l=[0, 0, 2], r=[2, 3, 5])
    ic(solution)
