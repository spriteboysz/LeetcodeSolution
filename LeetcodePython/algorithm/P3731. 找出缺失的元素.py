#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-12-14 22:33
FileName: P3731. 找出缺失的元素.py
Description:
"""
from typing import List


class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        seen = set(nums)
        maximum, minimum = max(seen), min(seen)
        return [num for num in range(minimum, maximum + 1) if num not in seen]


if __name__ == '__main__':
    s = Solution().findMissingElements(nums=[1, 4, 2, 5])
    print(s)
