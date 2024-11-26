#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-25 23:13
FileName: P2190. 数组中紧跟 key 之后出现最频繁的数字
Description:
"""
from typing import List
from collections import Counter

class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        nums2 = [nums[i + 1] for i in range(0, len(nums) - 1) if nums[i] == key]
        counter = Counter(nums2)
        maximum = max(counter.values())
        return [num for num, cnt in counter.items() if cnt == maximum][0]


if __name__ == '__main__':
    solution = Solution().mostFrequent(nums=[1, 100, 200, 1, 100], key=1)
    print(solution)
