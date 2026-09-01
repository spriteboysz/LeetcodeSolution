#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-01 21:14
FileName: LCP/P3159. 查询数组中元素的出现位置.py
Description: 
"""
from typing import List


class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        indexes = [i for i, num in enumerate(nums) if num == x]
        positions = []
        for query in queries:
            try:
                positions.append(indexes[query - 1])
            except IndexError:
                positions.append(-1)
        return positions


if __name__ == '__main__':
    solution = Solution().occurrencesOfElement(nums=[1, 3, 1, 7], queries=[1, 3, 2, 4], x=1)
    print(solution)
