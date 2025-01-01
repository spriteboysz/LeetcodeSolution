#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-01 19:27
FileName: LCR 076. 数组中的第 K 个最大元素
Description:
"""
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]


if __name__ == '__main__':
    solution = Solution().findKthLargest(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4)
    print(solution)
