#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-10-12 16:19
FileName: P3684. 至多 K 个不同元素的最大和.py
Description:
"""
from typing import List


class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        return sorted(set(nums), reverse=True)[:k]


if __name__ == '__main__':
    s = Solution().maxKDistinct(nums=[84, 93, 100, 77, 90], k=3)
    print(s)
