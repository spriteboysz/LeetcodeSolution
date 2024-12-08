#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-08 23:34
FileName: P0496. 下一个更大元素 I
Description:
"""
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        for i, num in enumerate(nums2):
            for num2 in nums2[i + 1:]:
                if num < num2:
                    dic[num] = num2
                    break
            else:
                dic[num] = -1
        return [dic[num] for num in nums1]


if __name__ == '__main__':
    solution = Solution().nextGreaterElement(nums1=[4, 1, 2], nums2=[1, 3, 4, 2])
    print(solution)
