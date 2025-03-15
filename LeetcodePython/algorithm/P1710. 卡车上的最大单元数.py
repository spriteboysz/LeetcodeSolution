#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-15 20:01
FileName: algorithm/P1710. 卡车上的最大单元数.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda el: el[1], reverse=True)
        units = 0
        for num, unit in boxTypes:
            if truckSize >= num:
                units += num * unit
                truckSize -= num
            else:
                units += truckSize * unit
                break
        return units


if __name__ == '__main__':
    solution = Solution().maximumUnits(boxTypes=[[5, 10], [2, 5], [4, 7], [3, 9]], truckSize=10)
    ic(solution)
