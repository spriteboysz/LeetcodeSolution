#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-04-07 23:26
FileName: P3737. 统计主要元素子数组数目 I.py
Description:
"""
from typing import List


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        nums = [num == target for num in nums]
        cnt = 0
        for left in range(len(nums)):
            for right in range(left, len(nums)):
                if sum(nums[left:right + 1]) >= (right - left) / 2:
                    cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().countMajoritySubarrays(nums=[1, 1, 1, 1], target=1)
    print(solution)
