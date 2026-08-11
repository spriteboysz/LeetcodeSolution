#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-10 22:54
FileName: P2442. 反转之后不同整数的数目.py
Description:
"""
from typing import List


class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        nums.extend([int(str(num)[::-1]) for num in nums])
        return len(set(nums))


if __name__ == '__main__':
    solution = Solution().countDistinctIntegers(nums=[1, 13, 10, 12, 31])
    print(solution)
