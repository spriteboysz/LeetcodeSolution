#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-06 18:21
FileName: P0217. 存在重复元素.py
Description:
"""
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


if __name__ == '__main__':
    solution = Solution().containsDuplicate([1, 2, 2, 1])
    print(solution)
