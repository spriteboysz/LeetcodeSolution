#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-05-31 16:19
FileName: P3834. 合并相邻且相等的元素.py
Description:
"""
from typing import List


class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        stack = []
        for num in nums:
            while stack and stack[-1] == num:
                stack.pop()
                num *= 2
            stack.append(num)
        return stack


if __name__ == '__main__':
    solution = Solution().mergeAdjacent(nums=[3, 1, 1, 2])
    print(solution)
