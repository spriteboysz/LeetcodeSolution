#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-08 23:35
FileName: P1619. 删除某些元素后的数组均值
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        return sum(arr[int(0.05 * len(arr)):int(0.95 * len(arr))]) / (len(arr) * 0.9)


if __name__ == '__main__':
    solution = Solution().trimMean([6, 2, 7, 5, 1, 2, 0, 3, 10, 2, 5, 0, 5, 5, 0, 8, 7, 6, 8, 0])
    ic(solution)
