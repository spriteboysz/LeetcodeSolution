#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-31 21:56
FileName: P1550. 存在连续三个奇数的数组
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        return any(arr[i - 2] % 2 == 1 and arr[i - 1] % 2 == 1 and arr[i] % 2 == 1 for i in range(2, len(arr)))


if __name__ == '__main__':
    solution = Solution().threeConsecutiveOdds(arr=[1, 2, 34, 3, 4, 5, 7, 23, 12])
    ic(solution)
