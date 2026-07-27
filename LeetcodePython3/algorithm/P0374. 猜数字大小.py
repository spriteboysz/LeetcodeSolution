#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-26 20:50
FileName: P0374. 猜数字大小.py
Description:
"""


def guess(num: int) -> int:
    ...


class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            if guess(mid) == 0:
                return mid
            if guess(mid) == 1:
                left = mid + 1
            else:
                right = mid - 1
        raise ValueError('Error')


if __name__ == '__main__':
    solution = Solution()
    print(solution)
