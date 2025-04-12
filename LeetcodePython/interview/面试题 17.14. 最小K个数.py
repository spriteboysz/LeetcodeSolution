#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-12 12:25
FileName: interview/面试题 17.14. 最小K个数.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        return sorted(arr)[:k]


if __name__ == '__main__':
    solution = Solution().smallestK(arr=[1, 3, 5, 7, 2, 4, 6, 8], k=4)
    ic(solution)
