#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-08 22:44
FileName: LCR/LCR 167. 招式拆解 I.py
Description: 
"""

from icecream import ic


class Solution:
    def dismantlingAction(self, arr: str) -> int:
        maximum, left = 0, 0
        for right in range(len(arr)):
            while arr[right] in arr[left:right]:
                left += 1
            maximum = max(maximum, right - left + 1)
        return maximum


if __name__ == '__main__':
    solution = Solution().dismantlingAction(arr="dbascDdad")
    ic(solution)
