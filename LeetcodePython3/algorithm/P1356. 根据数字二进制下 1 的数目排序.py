#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-20 10:20
FileName: P1356. 根据数字二进制下 1 的数目排序.py
Description:
"""
from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda num: (num.bit_count(), num))


if __name__ == '__main__':
    solution = Solution().sortByBits(arr = [0,1,2,3,4,5,6,7,8])
    print(solution)
