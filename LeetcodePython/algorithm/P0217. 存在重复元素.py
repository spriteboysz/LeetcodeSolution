#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-10 22:45
FileName: P0217. 存在重复元素
Description:
"""
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) > len(set(nums))


if __name__ == '__main__':
    solution = Solution().containsDuplicate([1, 2, 1])
    print(solution)
