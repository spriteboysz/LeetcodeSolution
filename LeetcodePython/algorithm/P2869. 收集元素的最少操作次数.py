#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-27 22:45
FileName: P2869. 收集元素的最少操作次数
Description:
"""
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        sequence = {num: len(nums) - i for i, num in enumerate(nums)}
        return max([sequence.get(i + 1) for i in range(k)])


if __name__ == '__main__':
    solution = Solution().minOperations(nums=[3, 1, 5, 4, 2], k=2)
    print(solution)
