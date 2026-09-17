#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-16 13:22
FileName: algorithm/P1710. 卡车上的最大单元数.py
Description: 
"""
from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda b: b[1], reverse=True)
        count = 0
        for cnt, size in boxTypes:
            if cnt <= truckSize:
                truckSize -= cnt
                count += cnt * size
            else:
                count += min(cnt, truckSize) * size
                break
        return count


if __name__ == '__main__':
    solution = Solution().maximumUnits(boxTypes=[[5, 10], [2, 5], [4, 7], [3, 9]], truckSize=10)
    print('<None>' if solution is None else f'{solution=}')
