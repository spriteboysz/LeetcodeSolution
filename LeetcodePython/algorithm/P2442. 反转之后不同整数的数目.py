#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-05 13:03
FileName: P2442. 反转之后不同整数的数目
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        seen = set(nums)
        seen.update({int(str(num)[::-1]) for num in seen})
        return len(seen)


if __name__ == '__main__':
    solution = Solution().countDistinctIntegers(nums=[1, 13, 10, 12, 31])
    ic(solution)
