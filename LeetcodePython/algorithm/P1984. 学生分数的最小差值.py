#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-23 22:30
FileName: P1984. 学生分数的最小差值
Description:
"""
from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        return min([num - nums[i] for i, num in enumerate(nums[k - 1:])])


if __name__ == '__main__':
    solution = Solution().minimumDifference(nums=[9, 4, 1, 7], k=2)
    print(solution)
