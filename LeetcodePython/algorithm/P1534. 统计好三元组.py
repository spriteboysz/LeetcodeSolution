#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-06 23:31
FileName: P1534. 统计好三元组
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        cnt = 0
        for k, num3 in enumerate(arr):
            for j, num2 in enumerate(arr[:k]):
                for _, num1 in enumerate(arr[:j]):
                    if abs(num1 - num2) <= a and abs(num2 - num3) <= b and abs(num1 - num3) <= c:
                        cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().countGoodTriplets(arr=[3, 0, 1, 1, 9, 7], a=7, b=2, c=3)
    ic(solution)
