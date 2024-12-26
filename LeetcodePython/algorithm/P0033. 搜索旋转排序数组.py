#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-26 23:28
FileName: P0033. 搜索旋转排序数组
Description:
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i, num in enumerate(nums):
            if num == target:
                return i
        return -1


if __name__ == '__main__':
    solution = Solution().search([4, 5, 6, 7, 0, 1, 2], 0)
    print(solution)
