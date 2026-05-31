#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-05-31 15:29
FileName: P3936. 将 0 移到末尾的最少交换次数.py
Description:
"""


class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        cnt = nums.count(0)
        if cnt == 0:
            return 0
        return cnt - nums[-cnt:].count(0)


if __name__ == '__main__':
    solution = Solution().minimumSwaps(nums=[0, 1, 0, 3, 12])
    print(solution)
