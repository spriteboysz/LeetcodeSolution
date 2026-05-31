#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-05-17 09:06
FileName: P3917. 统计下标的相反奇偶性得分.py
Description:
"""


class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        flags = [num % 2 == 0 for num in nums]
        return [sum(flag1 ^ flag2 for flag2 in flags[i + 1:]) for i, flag1 in enumerate(flags)]


if __name__ == '__main__':
    solution = Solution().countOppositeParity(nums=[1, 2, 3, 4])
    print(solution)
