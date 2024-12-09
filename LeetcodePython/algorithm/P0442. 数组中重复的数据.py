#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-10 00:06
FileName: P0442. 数组中重复的数据
Description:
"""
from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicate = []
        for num in nums:
            num = abs(num)
            if nums[num - 1] < 0:
                duplicate.append(num)
            nums[num - 1] = -abs(nums[num - 1])
        return [abs(num) for num in duplicate]


if __name__ == '__main__':
    solution = Solution().findDuplicates(nums=[4, 3, 2, 7, 8, 2, 3, 1])
    print(solution)
