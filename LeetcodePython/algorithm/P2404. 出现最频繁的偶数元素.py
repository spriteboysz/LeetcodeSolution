#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-26 22:52
FileName: P2404. 出现最频繁的偶数元素
Description:
"""
from typing import List
from collections import Counter


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        counter = Counter([num for num in nums if num % 2 == 0])
        if not counter:
            return -1
        maximum = max(counter.values())
        return min([num for num, cnt in counter.items() if cnt == maximum])

if __name__ == '__main__':
    solution = Solution().mostFrequentEven([0, 1, 2, 2, 4, 4, 1])
    print(solution)
