#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-26 23:34
FileName: P0034. 在排序数组中查找元素的第一个和最后一个位置
Description:
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        index = [i for i, num in enumerate(nums) if num == target]
        return [index[0], index[-1]] if index else [-1, -1]


if __name__ == '__main__':
    solution = Solution().searchRange(nums=[5, 7, 7, 8, 8, 10], target=8)
    print(solution)
