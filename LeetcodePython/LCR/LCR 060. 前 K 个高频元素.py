#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-01 09:57
FileName: LCR 060. 前 K 个高频元素
Description:
"""
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        return sorted(set(nums), key=lambda el: counter.get(el), reverse=True)[:k]


if __name__ == '__main__':
    solution = Solution().topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2)
    print(solution)
