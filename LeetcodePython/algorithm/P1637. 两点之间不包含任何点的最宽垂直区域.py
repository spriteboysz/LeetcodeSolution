#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-24 11:25
FileName: P1637. 两点之间不包含任何点的最宽垂直区域
Description:
"""
from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        nums = sorted(map(lambda el: el[0], points))
        return max(nums[i] - nums[i - 1] for i in range(1, len(nums)))


if __name__ == '__main__':
    solution = Solution().maxWidthOfVerticalArea(points=[[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]])
    print(solution)
