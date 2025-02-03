#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-03 18:12
FileName: P1217. 玩筹码
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        even, odd = 0, 0
        for num in position:
            if num % 2 == 0:
                odd += 1
            else:
                even += 1
        return min(odd, even)


if __name__ == '__main__':
    solution = Solution().minCostToMoveChips(position=[2, 2, 2, 3, 3])
    ic(solution)
