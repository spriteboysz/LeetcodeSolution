#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-16 20:18
FileName: P0367. 有效的完全平方数
Description:
"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 0, num
        while left <= right:
            mid = left + (right - left) // 2
            res = mid * mid
            if res == num and isinstance(res, int):
                return True
            elif res < num:
                left = mid + 1
            else:
                right = mid - 1
        return False


if __name__ == '__main__':
    solution = Solution().isPerfectSquare(25)
    print(solution)
