#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-04 22:56
FileName: P3432. 统计元素和差值为偶数的分区方案.py
Description:
"""
from typing import List


class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        acc, total, cnt = 0, sum(nums), 0
        for i, num in enumerate(nums[:-1]):
            acc += num
            if abs(total - acc - acc) % 2 == 0:
                cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().countPartitions(nums=[10, 10, 3, 7, 6])
    print(solution)
