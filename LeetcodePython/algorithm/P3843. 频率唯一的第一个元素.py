#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-03-01 21:48
FileName: P3843. 频率唯一的第一个元素.py
Description:
"""
from typing import List
from collections import Counter


class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        count1 = Counter(nums)
        count2 = Counter(count1.values())
        for num in nums:
            if count2.get(count1.get(num)) == 1:
                return num
        return -1


if __name__ == '__main__':
    s = Solution().firstUniqueFreq(nums=[20, 10, 30, 30])
    print(s)
