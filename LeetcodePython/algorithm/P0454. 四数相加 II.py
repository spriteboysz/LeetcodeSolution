#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-06-11 22:13
FileName: algorithm/P0454. 四数相加 II.py
Description: 
"""
from collections import defaultdict
from typing import List

from icecream import ic


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        def process(numbers1, numbers2):
            dic = defaultdict(int)
            for num1 in numbers1:
                for num2 in numbers2:
                    dic[num1 + num2] += 1
            return dic

        dic1 = process(nums1, nums2)
        dic2 = process(nums3, nums4)
        return sum(v * dic2.get(-k, 0) for k, v in dic1.items())


if __name__ == '__main__':
    solution = Solution().fourSumCount(nums1=[1, 2], nums2=[-2, -1], nums3=[-1, 2], nums4=[0, 2])
    ic(solution)
