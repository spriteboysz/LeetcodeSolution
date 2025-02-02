#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-01 22:03
FileName: P2176. 统计数组中相等且可以被整除的数对
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        cnt = 0
        for j, num1 in enumerate(nums):
            for i, num2 in enumerate(nums[:j]):
                if num1 == num2 and (i * j) % k == 0:
                    cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().countPairs(nums=[3, 1, 2, 2, 2, 1, 3], k=2)
    ic(solution)
