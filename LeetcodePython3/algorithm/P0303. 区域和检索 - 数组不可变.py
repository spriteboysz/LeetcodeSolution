#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-19 22:33
FileName: P0303. 区域和检索 - 数组不可变.py
Description:
"""
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.pref, acc = [], 0
        for num in nums:
            acc += num
            self.pref.append(acc)

    def sumRange(self, left: int, right: int) -> int:
        return self.pref[right] - (self.pref[left - 1] if left != 0 else 0)


if __name__ == '__main__':
    solution = NumArray([-2, 0, 3, -5, 2, -1])
    print(solution.sumRange(0, 5))
