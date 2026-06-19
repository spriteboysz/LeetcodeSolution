#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-19 12:25
FileName: P2119. 反转两次的数字.py
Description:
"""


class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num == 0:
            return True
        return num % 10 != 0


if __name__ == '__main__':
    solution = Solution().isSameAfterReversals(100)
    print(solution)
