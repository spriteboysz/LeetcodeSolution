#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-29 14:11
FileName: LCR 121. 寻找目标值 - 二维数组
Description:
"""
from typing import List


class Solution:
    def findTargetIn2DPlants(self, plants: List[List[int]], target: int) -> bool:
        for i, plant in enumerate(plants):
            for num in plant:
                if num == target:
                    return True
        return False


if __name__ == '__main__':
    solution = Solution().findTargetIn2DPlants(plants=[[2, 3, 6, 8], [4, 5, 8, 9], [5, 9, 10, 12]], target=8)
    print(solution)
