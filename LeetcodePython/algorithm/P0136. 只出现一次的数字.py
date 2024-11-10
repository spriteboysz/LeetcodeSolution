#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-10 19:57
FileName: P0136. 只出现一次的数字
Description:
"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single = 0
        for num in nums:
            single ^= num
        return single


if __name__ == '__main__':
    solution = Solution().singleNumber(nums=[4, 1, 2, 1, 2])
    print(solution)
