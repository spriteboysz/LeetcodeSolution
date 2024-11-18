#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-18 23:00
FileName: P1295. 统计位数为偶数的数字
Description:
"""
from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum([len(str(num)) % 2 == 0 for num in nums])


if __name__ == '__main__':
    solution = Solution().findNumbers(nums=[12, 345, 2, 6, 7896])
    print(solution)
