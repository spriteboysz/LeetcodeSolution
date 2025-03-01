#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-26 22:47
FileName: P1387. 将整数按权重排序
Description:
"""

from icecream import ic


class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def calc(num):
            cnt = 0
            while num > 1:
                if num % 2 == 0:
                    num //= 2
                else:
                    num = num * 3 + 1
                cnt += 1
            return cnt

        return sorted(range(lo, hi + 1), key=calc)[k - 1]


if __name__ == '__main__':
    solution = Solution().getKth(lo=7, hi=11, k=4)
    ic(solution)
