#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-04 08:43
FileName: LC/LCR 121. 寻找目标值 - 二维数组.py
Description: 
"""
from typing import List


class Solution:
    def findTargetIn2DPlants(self, plants: List[List[int]], target: int) -> bool:
        for plant in plants:
            if not plant:
                return False
            if plant[0] <= target <= plant[-1]:
                if target in plant:
                    return True
        return False


if __name__ == '__main__':
    solution = Solution().findTargetIn2DPlants(
        plants=[
            [2, 3, 6, 8],
            [4, 5, 8, 9],
            [5, 9, 10, 12]
        ],
        target=4)
    print(solution)
