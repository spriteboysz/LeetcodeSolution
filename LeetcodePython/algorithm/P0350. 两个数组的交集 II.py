#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-13 23:15
FileName: P0350. 两个数组的交集 II
Description:
"""
from typing import List
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter1, counter2 = Counter(nums1), Counter(nums2)
        seen = []
        for num, cnt in counter1.items():
            if (minimum := min(cnt, counter2.get(num, 0))) > 0:
                seen.extend([num] * minimum)
        return seen


if __name__ == '__main__':
    solution = Solution().intersect(nums1=[1, 2, 2, 1], nums2=[2, 2])
    print(solution)
