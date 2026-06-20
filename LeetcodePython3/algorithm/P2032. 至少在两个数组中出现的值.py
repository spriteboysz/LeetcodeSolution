#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-20 16:55
FileName: P2032. 至少在两个数组中出现的值.py
Description:
"""
from collections import defaultdict
from typing import List


class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        dic = defaultdict(set)
        for i, nums in enumerate([nums1, nums2, nums3]):
            for num in nums:
                dic[num].add(i)
        return [k for k, v in dic.items() if len(v) >= 2]


if __name__ == '__main__':
    solution = Solution().twoOutOfThree(nums1=[1, 1, 3, 2], nums2=[2, 3], nums3=[3])
    print(solution)
