#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-18 11:46
FileName: P0496. 下一个更大元素 I.py
Description:
"""
from typing import List
from collections import defaultdict


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = defaultdict(int)
        for i, num1 in enumerate(nums2):
            for num2 in nums2[i + 1:]:
                if num2 > num1:
                    dic[num1] = num2
                    break
            else:
                dic[num1] = -1
        return [dic.get(num, -1) for num in nums1]


if __name__ == '__main__':
    solution = Solution().nextGreaterElement(nums1=[4, 1, 2], nums2=[1, 3, 4, 2])
    print(solution)
