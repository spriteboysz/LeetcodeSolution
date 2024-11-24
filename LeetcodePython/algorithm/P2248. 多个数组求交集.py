#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-24 08:52
FileName: P2248. 多个数组求交集
Description:
"""
from typing import List
from functools import reduce


class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        seen = reduce(lambda nums1, nums2: set(nums1) & set(nums2), map(lambda el: set(el), nums))
        return sorted(list(seen))


if __name__ == '__main__':
    solution = Solution().intersection(nums=[[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]])
    print(solution)
