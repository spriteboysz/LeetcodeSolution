#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-24 20:52
FileName: P3005. 最大频率元素计数
Description:
"""
from typing import List
from collections import Counter


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = list(Counter(nums).values())
        maximum = max(counter)
        return sum([cnt for cnt in counter if cnt == maximum])


if __name__ == '__main__':
    solution = Solution().maxFrequencyElements(nums=[1, 2, 2, 3, 1, 4])
    print(solution)
