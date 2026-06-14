#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-14 14:45
FileName: P1437. 是否所有 1 都至少相隔 k 个元素.py
Description:
"""
from itertools import pairwise
from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        index = [i for i, num in enumerate(nums) if num == 1]
        return all(b - a - 1 >= k for a, b in pairwise(index))


if __name__ == '__main__':
    solution = Solution().kLengthApart(nums=[1, 1, 1, 0], k=2)
    print(solution)
