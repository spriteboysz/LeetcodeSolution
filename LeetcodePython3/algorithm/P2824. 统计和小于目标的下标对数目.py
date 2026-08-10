#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-09 19:11
FileName: P2824. 统计和小于目标的下标对数目.py
Description:
"""
from typing import List


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        cnt = 0
        for i, num1 in enumerate(nums):
            for num2 in nums[i + 1:]:
                if num1 + num2 >= target:
                    break
                cnt += 1

        return cnt


if __name__ == '__main__':
    solution = Solution().countPairs(nums=[-1, 1, 2, 3, 1], target=2)
    print(solution)
