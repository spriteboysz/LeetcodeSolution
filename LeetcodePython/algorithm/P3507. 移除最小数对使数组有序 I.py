#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-13 22:55
FileName: interview/P3507. 移除最小数对使数组有序 I.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        cnt = 0
        while any(nums[i] < nums[i - 1] for i in range(1, len(nums))):
            minimum = min(nums[i - 1] + nums[i] for i in range(1, len(nums)))
            for i in range(1, len(nums)):
                if nums[i - 1] + nums[i] == minimum:
                    nums[i - 1] += nums[i]
                    nums.pop(i)
                    break
            cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().minimumPairRemoval(nums=[5, 2, 3, 1])
    ic(solution)
