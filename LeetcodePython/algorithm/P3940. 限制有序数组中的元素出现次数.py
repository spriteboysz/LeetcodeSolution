#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-05-31 15:24
FileName: P3940. 限制有序数组中的元素出现次数.py
Description:
"""

from collections import Counter


class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        counter = Counter(nums)
        return sorted(sum([[num] * min(k, v) for num, v in counter.items()], []))


if __name__ == '__main__':
    solution = Solution().limitOccurrences(nums=[1, 1, 1, 2, 2, 3], k=2)
    print(solution)
