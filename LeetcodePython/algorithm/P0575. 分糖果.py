#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-10 22:39
FileName: P0575. 分糖果
Description:
"""
from typing import List


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(set(candyType)), len(candyType) // 2)


if __name__ == '__main__':
    solution = Solution().distributeCandies([1, 1, 2, 2, 3, 3])
    print(solution)
