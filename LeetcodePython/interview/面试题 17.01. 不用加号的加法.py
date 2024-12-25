#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-24 23:30
FileName: 面试题 17.01. 不用加号的加法
Description:
"""


class Solution:
    def add(self, a: int, b: int) -> int:
        return sum([a, b])


if __name__ == '__main__':
    solution = Solution().add(1, 1)
    print(solution)
