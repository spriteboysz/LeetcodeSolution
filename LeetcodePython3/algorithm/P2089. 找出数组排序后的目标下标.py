#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-20 11:34
FileName: P2089. 找出数组排序后的目标下标.py
Description:
"""
from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        return [i for i, num in enumerate(sorted(nums)) if num == target]


if __name__ == '__main__':
    solution = Solution().targetIndices(nums=[1, 2, 5, 2, 3], target=2)
    print(solution)
