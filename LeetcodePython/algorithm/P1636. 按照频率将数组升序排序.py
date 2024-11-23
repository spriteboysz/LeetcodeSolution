#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-23 22:19
FileName: P1636. 按照频率将数组升序排序
Description:
"""
from typing import List
from collections import Counter


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        return sorted(nums, key=lambda el: (counter[el], -el))


if __name__ == '__main__':
    solution = Solution().frequencySort(nums=[2, 3, 1, 3, 2])
    print(solution)
