#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-27 22:53
FileName: P2956. 找到两个数组中的公共元素
Description:
"""
from collections import Counter
from typing import List


class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)
        return [sum([counter1.get(k, 0) for k in counter2]), sum(counter2.get(k, 0) for k in counter1)]


if __name__ == '__main__':
    solution = Solution().findIntersectionValues(nums1=[4, 3, 2, 3, 1], nums2=[2, 2, 5, 2, 3, 6])
    print(solution)
