#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-28 16:38
FileName: P2231. 按奇偶性交换后的最大数字.py
Description:
"""


class Solution:
    def largestInteger(self, num: int) -> int:
        odd, even = [], []
        for ch in str(num):
            if int(ch) % 2 == 0:
                even.append(ch)
            else:
                odd.append(ch)
        even.sort()
        odd.sort()
        ss = []
        for i, ch in enumerate(str(num)):
            if int(ch) % 2 == 0:
                ss.append(even.pop())
            else:
                ss.append(odd.pop())
        return int(''.join(ss))


if __name__ == '__main__':
    solution = Solution().largestInteger(1234)
    print(solution)
