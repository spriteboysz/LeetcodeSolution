#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-20 21:30
FileName: P2570. 合并两个二维数组 - 求和法.py
Description:
"""
from collections import defaultdict
from typing import List


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        dic = defaultdict(int)
        for k, v in nums1 + nums2:
            dic[k] += v
        return sorted([[k, v] for k, v in dic.items()])


if __name__ == '__main__':
    solution = Solution().mergeArrays(nums1=[[1, 2], [2, 3], [4, 5]], nums2=[[1, 4], [3, 2], [4, 1]])
    print(solution)
