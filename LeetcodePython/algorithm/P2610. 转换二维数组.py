#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-07 21:29
FileName: P2610. 转换二维数组
Description:
"""
from collections import defaultdict
from typing import List

from icecream import ic


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1
        matrix = [[] for _ in range(max(dic.values()))]
        for k, v in dic.items():
            for i in range(v):
                matrix[i].append(k)
        return matrix


if __name__ == '__main__':
    solution = Solution().findMatrix(nums=[1, 3, 4, 1, 2, 3, 1])
    ic(solution)
