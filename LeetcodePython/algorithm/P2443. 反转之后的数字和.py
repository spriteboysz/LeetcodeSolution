#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-06 23:52
FileName: P2443. 反转之后的数字和
Description:
"""

from icecream import ic


class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        ranges = (i + int(str(i)[::-1]) for i in range(num + 1))
        for n in ranges:
            if n == num:
                return True
        return False


if __name__ == '__main__':
    solution = Solution().sumOfNumberAndReverse(443)
    ic(solution)
