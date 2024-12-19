#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-19 23:07
FileName: P1539. 第 k 个缺失的正整数
Description:
"""
from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        seen = set(arr)
        for i in range(1, 2001):
            if i not in seen:
                k -= 1
            if k == 0:
                return i
        return -1


if __name__ == '__main__':
    solution = Solution().findKthPositive(arr=[2, 3, 4, 7, 11], k=5)
    print(solution)
