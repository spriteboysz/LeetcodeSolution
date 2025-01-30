#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-29 21:08
FileName: P3432. 统计元素和差值为偶数的分区方案
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        left, right, cnt = 0, sum(nums), 0
        for num in nums[:-1]:
            left += num
            right -= num
            if (right - left) % 2 == 0:
                cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().countPartitions([10, 10, 3, 7, 6])
    ic(solution)
