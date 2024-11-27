#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-27 21:56
FileName: P2341. 数组能形成多少数对
Description:
"""
from functools import reduce
from typing import List
from collections import Counter


class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        cnt = (divmod(v, 2) for v in counter.values())
        return list(reduce(lambda el1, el2: (el1[0] + el2[0], el1[1] + el2[1]), cnt))


if __name__ == '__main__':
    solution = Solution().numberOfPairs(nums=[1, 3, 2, 1, 3, 2, 2])
    print(solution)
