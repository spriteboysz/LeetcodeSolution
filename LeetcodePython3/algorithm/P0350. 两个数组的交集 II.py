#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-06 19:47
FileName: P0350. 两个数组的交集 II.py
Description:
"""
from collections import Counter

from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1, count2 = Counter(nums1), Counter(nums2)
        ans = []
        for num, cnt in count1.items():
            ans.extend([num] * min(cnt, count2.get(num, 0)))
        return ans


if __name__ == '__main__':
    solution = Solution().intersect(nums1=[1, 2, 2, 1], nums2=[2, 2])
    print(solution)
