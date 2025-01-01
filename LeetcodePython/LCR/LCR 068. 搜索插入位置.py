#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-01 19:20
FileName: LCR 068. 搜索插入位置
Description:
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i, num in enumerate(nums):
            if num >= target:
                return i
        return len(nums)


if __name__ == '__main__':
    solution = Solution().searchInsert(nums=[1, 3, 5, 6], target=7)
    print(solution)
