#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-01 20:06
FileName: P0485. 最大连续 1 的个数
Description:
"""
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return max(map(len, ''.join(map(str, nums)).split('0')))


if __name__ == '__main__':
    solution = Solution().findMaxConsecutiveOnes(nums=[1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1])
    print(solution)
