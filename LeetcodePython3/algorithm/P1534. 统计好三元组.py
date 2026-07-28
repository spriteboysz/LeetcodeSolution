#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-27 23:44
FileName: P1534. 统计好三元组.py
Description:
"""
from typing import List


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        cnt = 0
        for i, num1 in enumerate(arr):
            for j, num2 in enumerate(arr[i + 1:], start=i + 1):
                if abs(num1 - num2) > a:
                    continue
                for num3 in arr[j + 1:]:
                    if abs(num2 - num3) <= b and abs(num1 - num3) <= c:
                        cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().countGoodTriplets(arr=[3, 0, 1, 1, 9, 7], a=7, b=2, c=3)
    print(solution)
