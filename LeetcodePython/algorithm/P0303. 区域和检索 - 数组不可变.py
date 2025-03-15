#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-14 23:07
FileName: algorithm/P0303. 区域和检索 - 数组不可变.py
Description: 
"""
from typing import List

from icecream import ic


class NumArray:

    def __init__(self, nums: List[int]):
        self.acc_nums, acc = [0], 0
        for num in nums:
            acc += num
            self.acc_nums.append(acc)

    def sumRange(self, left: int, right: int) -> int:
        return self.acc_nums[right + 1] - self.acc_nums[left]


if __name__ == '__main__':
    solution = NumArray([-2, 0, 3, -5, 2, -1])
    ic(solution.sumRange(0, 2))
    ic(solution.sumRange(2, 5))
    ic(solution.sumRange(0, 5))
