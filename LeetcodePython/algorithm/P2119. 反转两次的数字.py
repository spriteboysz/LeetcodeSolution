#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-17 21:37
FileName: P2119. 反转两次的数字
Description:
"""


class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num == 0:
            return True
        return num % 10 != 0


if __name__ == '__main__':
    solution = Solution().isSameAfterReversals(1600)
    print(solution)
