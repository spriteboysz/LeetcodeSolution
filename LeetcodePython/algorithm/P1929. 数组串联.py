#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-16 17:26
FileName: P1929. 数组串联
Description:
"""
from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return [*nums, *nums]


if __name__ == '__main__':
    solution = Solution().getConcatenation(nums=[1, 3, 2, 1])
    print(solution)
