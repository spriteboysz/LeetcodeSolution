#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-17 21:53
FileName: P1423. 可获得的最大点数
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        nums = cardPoints[:k][::-1]
        maximum = curr = sum(nums)
        for i, num in enumerate(nums):
            b = cardPoints[-1 - i]
            curr = curr - num + b
            maximum = max(maximum, curr)
        return maximum


if __name__ == '__main__':
    solution = Solution().maxScore(cardPoints=[1, 79, 80, 1, 1, 1, 200, 1], k=3)
    ic(solution)
