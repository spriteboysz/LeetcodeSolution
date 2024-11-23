#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-23 22:07
FileName: P1365. 有多少小于当前数字的数字
Description:
"""
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sort = sorted(nums, reverse=True)
        dic = {num: i for i, num in enumerate(sort)}
        return [len(nums) - dic[num] - 1 for num in nums]


if __name__ == '__main__':
    solution = Solution().smallerNumbersThanCurrent(nums=[8, 1, 2, 2, 3])
    print(solution)
