#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-20 22:18
FileName: P2769. 找出最大的可达成数字
Description:
"""


class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + 2 * t


if __name__ == '__main__':
    solution = Solution().theMaximumAchievableX(3, 2)
    print(solution)
