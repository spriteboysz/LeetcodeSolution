#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-10 22:28
FileName: P0169. 多数元素
Description:
"""
from typing import List
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        return sorted([(k, v) for k, v in counter.items()], key=lambda el: el[1])[-1][0]


if __name__ == '__main__':
    solution = Solution().majorityElement([3, 2, 3])
    print(solution)
