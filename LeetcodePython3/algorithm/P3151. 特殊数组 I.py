#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-20 18:47
FileName: P3151. 特殊数组 I.py
Description:
"""
from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        ss = ''.join(map(str, (num % 2 for num in nums)))
        return '00' not in ss and '11' not in ss


if __name__ == '__main__':
    solution = Solution().isArraySpecial(nums=[2, 1, 4])
    print(solution)
