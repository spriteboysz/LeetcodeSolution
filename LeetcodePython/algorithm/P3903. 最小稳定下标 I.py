#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-04-26 18:54
FileName: P3903. 最小稳定下标 I.py
Description:
"""


class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        assist = [[-1, -1] for _ in range(len(nums))]
        assist[0][0], assist[-1][-1] = nums[0], nums[-1]
        acc = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > acc:
                acc = nums[i]
            assist[i][0] = acc

        acc = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < acc:
                acc = nums[i]
            assist[i][-1] = acc
            "ss".startswith()

        for i, (m1, m2) in enumerate(assist):
            if m1 - m2 <= k:
                return i
        return -1


if __name__ == '__main__':
    solution = Solution().firstStableIndex(nums=[5, 0, 1, 4], k=3)
    print(solution)
