#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-23 21:30
FileName: P1200. 最小绝对差
Description:
"""
from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minimum = arr[1] - arr[0]
        for i in range(1, len(arr)):
            minimum = min(arr[i] - arr[i - 1], minimum)
        return [[arr[i - 1], arr[i]] for i in range(1, len(arr)) if arr[i] - arr[i - 1] == minimum]


if __name__ == '__main__':
    solution = Solution().minimumAbsDifference(arr=[4, 2, 1, 3])
    print(solution)
