#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-09 22:38
FileName: P2089. 找出数组排序后的目标下标
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        return [i for i, num in enumerate(sorted(nums)) if num == target]


if __name__ == '__main__':
    solution = Solution().targetIndices(nums=[1, 2, 5, 2, 3], target=2)
    ic(solution)
