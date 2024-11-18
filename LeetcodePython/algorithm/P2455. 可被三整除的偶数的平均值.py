#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-17 22:19
FileName: P2455. 可被三整除的偶数的平均值
Description:
"""
from typing import List


class Solution:
    def averageValue(self, nums: List[int]) -> int:
        values = [num for num in nums if num % 6 == 0]
        return sum(values) // len(values) if values else 0


if __name__ == '__main__':
    solution = Solution().averageValue(nums=[1, 3, 6, 10, 12, 15])
    print(solution)
