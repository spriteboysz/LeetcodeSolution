#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-03 20:33
FileName: P3285. 找到稳定山的下标
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        return [i for i in range(1, len(height)) if height[i - 1] > threshold]


if __name__ == '__main__':
    solution = Solution().stableMountains(height=[10, 1, 10, 1, 10], threshold=3)
    ic(solution)
