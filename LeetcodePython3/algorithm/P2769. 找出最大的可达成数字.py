#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-08 22:41
FileName: P2769. 找出最大的可达成数字.py
Description:
"""


class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + t * 2


if __name__ == '__main__':
    solution = Solution().theMaximumAchievableX(4, 1)
    print(solution)
