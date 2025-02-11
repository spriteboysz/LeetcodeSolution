#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-10 23:09
FileName: P2657. 找到两个数组的前缀公共数组
Description:
"""
from collections import Counter
from typing import List

from icecream import ic


class Solution:
    def findThePrefixCommonArray(self, nums1: List[int], nums2: List[int]) -> List[int]:
        commons = []
        for i in range(len(nums1)):
            counter1 = Counter(nums1[:i + 1])
            counter2 = Counter(nums2[:i + 1])
            common = sum(min(v, counter2.get(k, 0)) for k, v in counter1.items())
            commons.append(common)
        return commons


if __name__ == '__main__':
    solution = Solution().findThePrefixCommonArray(nums1=[1, 3, 2, 4], nums2=[3, 1, 2, 4])
    ic(solution)
