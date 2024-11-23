#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-23 22:38
FileName: P2148. 元素计数
Description:
"""
from typing import List


class Solution:
    def countElements(self, nums: List[int]) -> int:
        maximum, minimum = max(nums), min(nums)
        return len([num for num in nums if num != maximum and num != minimum])


if __name__ == '__main__':
    solution = Solution().countElements(nums=[11, 7, 2, 15])
    print(solution)
