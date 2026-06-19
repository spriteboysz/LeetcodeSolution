#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-19 20:58
FileName: P2544. 交替数字和.py
Description:
"""


class Solution:
    def alternateDigitSum(self, n: int) -> int:
        ans, flag = 0, 1
        for digit in str(n):
            ans += int(digit) * flag
            flag *= -1
        return ans


if __name__ == '__main__':
    solution = Solution().alternateDigitSum(521)
    print(solution)
