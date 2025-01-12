#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-12 18:43
FileName: P2562. 找出数组的串联值
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        num, n = 0, len(nums)
        for i in range(n // 2 + 1):
            if i == n // 2:
                if n % 2 == 1:
                    num += nums[i]
            else:
                # num += int(str(nums[i]) + str(nums[n - 1 - i]))
                num += nums[i] * (10 ** len(str(nums[n - 1 - i]))) + nums[n - 1 - i]
        return num


if __name__ == '__main__':
    solution = Solution().findTheArrayConcVal(nums=[7, 52, 2, 4])
    ic(solution)
