#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-03 09:32
FileName: algorithm/P3996. 偶数次骑士移动.py
Description: 
"""


class Solution:
    def canReach(self, start: list[int], target: list[int]) -> bool:
        return (start[0] + start[1]) % 2 == (target[0] + target[1]) % 2


if __name__ == '__main__':
    solution = Solution().canReach([4, 5], [6, 6])
    print(solution)
