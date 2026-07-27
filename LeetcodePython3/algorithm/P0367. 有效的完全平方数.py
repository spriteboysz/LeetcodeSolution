#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-26 20:41
FileName: P0367. 有效的完全平方数.py
Description:
"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, num
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == num:
                return True
            if mid * mid < num:
                left = mid + 1
            else:
                right = mid - 1
        return False


if __name__ == '__main__':
    solution = Solution().isPerfectSquare(1)
    print(solution)
