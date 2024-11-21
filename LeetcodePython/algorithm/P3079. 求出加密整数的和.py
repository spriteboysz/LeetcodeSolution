#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-21 22:44
FileName: P3079. 求出加密整数的和
Description:
"""
from typing import List


class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        return sum([int(max(str(num)) * len(str(num))) for num in nums])


if __name__ == '__main__':
    solution = Solution().sumOfEncryptedInt([10, 21, 31])
    print(solution)
