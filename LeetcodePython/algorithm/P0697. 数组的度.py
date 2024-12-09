#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-08 23:44
FileName: P0697. 数组的度
Description:
"""
from typing import List
from collections import defaultdict


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        dic = defaultdict(list)
        for i, num in enumerate(nums):
            dic[num].append(i)
        maximum = max(map(len, dic.values()))
        minimum = len(nums)
        for lst in dic.values():
            if len(lst) == maximum:
                minimum = min(minimum, lst[-1] - lst[0] + 1)
        return minimum


if __name__ == '__main__':
    solution = Solution().findShortestSubArray([1, 2, 2, 3, 1, 4, 2])
    print(solution)
