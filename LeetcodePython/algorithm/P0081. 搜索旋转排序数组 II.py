#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-11 22:22
FileName: P0081. 搜索旋转排序数组 II
Description:
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        return target in set(nums)


if __name__ == '__main__':
    solution = Solution().search(nums=[2, 5, 6, 0, 0, 1, 2], target=0)
    print(solution)
