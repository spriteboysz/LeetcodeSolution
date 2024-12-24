#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-23 23:07
FileName: 面试题 16.07. 最大数值
Description:
"""


class Solution:
    def maximum(self, a: int, b: int) -> int:
        return ((a + b) + abs(a - b)) // 2


if __name__ == '__main__':
    solution = Solution().maximum(-2, -1)
    print(solution)
