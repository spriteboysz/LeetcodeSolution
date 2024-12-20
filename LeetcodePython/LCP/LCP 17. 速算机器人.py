#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-20 22:35
FileName: LCP 17. 速算机器人
Description:
"""


class Solution:
    def calculate(self, s: str) -> int:
        x, y = 1, 0
        for ch in s:
            if ch == 'A':
                x = 2 * x + y
            else:
                y = 2 * y + x
        return x + y


if __name__ == '__main__':
    solution = Solution().calculate('AB')
    print(solution)
