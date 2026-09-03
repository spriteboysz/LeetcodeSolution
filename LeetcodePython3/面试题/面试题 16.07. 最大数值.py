#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-03 10:20
FileName: 面试题/面试题 16.07. 最大数值.py
Description: 
"""


class Solution:
    def maximum(self, a: int, b: int) -> int:
        return max(a, b)


if __name__ == '__main__':
    solution = Solution().maximum(1, 2)
    print(solution)
