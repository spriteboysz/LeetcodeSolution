#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-24 21:55
FileName: P1437. 是否所有 1 都至少相隔 k 个元素
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        index = [i for i, num in enumerate(nums) if num == 1]
        for i in range(1, len(index)):
            if index[i] - index[i - 1] - 1 < k:
                return False
        return True


if __name__ == '__main__':
    solution = Solution().kLengthApart(nums=[1, 0, 0, 0, 1, 0, 1], k=2)
    ic(solution)
