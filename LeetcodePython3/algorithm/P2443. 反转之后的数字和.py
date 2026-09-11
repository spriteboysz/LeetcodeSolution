#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-10 09:26
FileName: algorithm/P2443. 反转之后的数字和.py
Description: 
"""


class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        for i in range(num, -1, -1):
            if i + int(str(i)[::-1]) == num:
                return True
        return False


if __name__ == '__main__':
    solution = Solution().sumOfNumberAndReverse(443)
    print('<None>' if solution is None else f'{solution=}')
