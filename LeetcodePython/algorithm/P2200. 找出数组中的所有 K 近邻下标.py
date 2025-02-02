#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-01 22:07
FileName: P2200. 找出数组中的所有 K 近邻下标
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        indices = [i for i, num in enumerate(nums) if num == key]
        k_indices = []
        for index in indices:
            k_indices.extend(list(range(index - k, index + k + 1)))
        return sorted(set(k_indices) & set(range(len(nums))))


if __name__ == '__main__':
    solution = Solution().findKDistantIndices(nums=[3, 4, 9, 1, 3, 9, 5], key=9, k=1)
    ic(solution)
