#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-24 11:55
FileName: P2784. 检查数组是否是好的
Description:
"""
from typing import List


class Solution:
    def isGood(self, nums: List[int]) -> bool:
        count = [0] * (len(nums))
        for num in nums:
            if num >= len(nums):
                return False
            count[num] += 1
        for cnt in count[1:-1]:
            if cnt != 1:
                return False
        return count[-1] == 2


if __name__ == '__main__':
    solution = Solution().isGood(nums=[1, 3, 3, 2])
    print(solution)
