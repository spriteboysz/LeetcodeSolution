#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-08 23:50
FileName: P0229. 多数元素 II
Description:
"""
from typing import List
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        return [num for num in counter if counter[num] * 3 > len(nums)]


if __name__ == '__main__':
    solution = Solution().majorityElement([1, 2])
    print(solution)
