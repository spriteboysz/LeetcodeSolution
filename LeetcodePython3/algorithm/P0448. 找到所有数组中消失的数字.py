#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-14 14:12
FileName: P0448. 找到所有数组中消失的数字.py
Description:
"""
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return list(set(range(1, len(nums) + 1)) - set(nums))


if __name__ == '__main__':
    solution = Solution().findDisappearedNumbers(nums = [4,3,2,7,8,2,3,1])
    print(solution)
