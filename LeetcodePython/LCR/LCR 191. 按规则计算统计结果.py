#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-02 23:35
FileName: LCR 191. 按规则计算统计结果
Description:
"""
from typing import List


class Solution:
    def statisticalResult(self, arrayA: List[int]) -> List[int]:
        if arrayA.count(0) >= 2:
            return [0] * len(arrayA)

        product = 1
        for num in arrayA:
            if num != 0:
                product *= num
        if arrayA.count(0) == 1:
            for i, num in enumerate(arrayA):
                if num == 0:
                    arrayA[i] = product
                else:
                    arrayA[i] = 0
            return arrayA
        return [product // num for num in arrayA]


if __name__ == '__main__':
    solution = Solution().statisticalResult([2, 4, 6, 8, 10])
    print(solution)
