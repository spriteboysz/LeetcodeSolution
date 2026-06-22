#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-21 20:33
FileName: P3300. 替换为数位和以后的最小元素.py
Description:
"""
from typing import List


class Solution:
    def minElement(self, nums: List[int]) -> int:
        return min(sum(map(int, (digit for digit in str(num)))) for num in nums)


if __name__ == '__main__':
    solution = Solution().minElement(nums=[999, 19, 199])
    print(solution)
