#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-24 23:06
FileName: P2032. 至少在两个数组中出现的值
Description:
"""
from typing import List
from collections import defaultdict


class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        dic = defaultdict(int)
        for num in [*set(nums1), *set(nums2), *set(nums3)]:
            dic[num] += 1
        return [num for num, cnt in dic.items() if cnt >= 2]


if __name__ == '__main__':
    solution = Solution().twoOutOfThree(nums1=[1, 1, 3, 2], nums2=[2, 3], nums3=[3])
    print(solution)
