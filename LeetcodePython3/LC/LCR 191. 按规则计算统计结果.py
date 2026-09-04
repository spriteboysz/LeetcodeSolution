#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-04 08:23
FileName: LC/LCR 191. 按规则计算统计结果.py
Description: 
"""
from typing import List


class Solution:
    def statisticalResult(self, arrayA: List[int]) -> List[int]:
        count0 = sum(num == 0 for num in arrayA)
        if count0 >= 2:
            return [0] * len(arrayA)
        product = 1
        for num in arrayA:
            if num == 0:
                continue
            product *= num
        if count0 == 1:
            return [0 if num != 0 else product for num in arrayA]
        return [product // num for num in arrayA]


if __name__ == '__main__':
    solution = Solution().statisticalResult([2, 4, 6, 8, 10])
    print(solution)
