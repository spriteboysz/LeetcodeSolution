#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-20 13:37
FileName: P2404. 出现最频繁的偶数元素.py
Description:
"""

from typing import List, Counter


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        counter = Counter(num for num in nums if num % 2 == 0)
        maximum = max(counter.values(), default=-1)
        return min([num for num, cnt in counter.items() if cnt == maximum], default=-1)


if __name__ == '__main__':
    solution = Solution().mostFrequentEven(nums=[2, 4])
    print(solution)
