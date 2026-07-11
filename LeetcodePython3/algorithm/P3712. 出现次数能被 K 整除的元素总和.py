#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-11 10:54
FileName: P3712. 出现次数能被 K 整除的元素总和.py
Description:
"""
from typing import List, Counter


class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        return sum(num * cnt for num, cnt in counter.items() if cnt % k == 0)


if __name__ == '__main__':
    solution = Solution().sumDivisibleByK(nums=[1, 2, 2, 3, 3, 3, 3, 4], k=2)
    print(solution)
