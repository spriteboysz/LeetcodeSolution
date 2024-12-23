#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-22 22:52
FileName: 面试题 08.03. 魔术索引
Description:
"""
from typing import List


class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            if i == num:
                return i
        return -1


if __name__ == '__main__':
    solution = Solution().findMagicIndex(nums=[0, 2, 3, 4, 5])
    print(solution)
