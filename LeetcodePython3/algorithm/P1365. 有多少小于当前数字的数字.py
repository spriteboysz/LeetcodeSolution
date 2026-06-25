#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-24 23:41
FileName: P1365. 有多少小于当前数字的数字.py
Description:
"""
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dic = {}
        for i, num in enumerate(sorted(nums)):
            if num not in dic:
                dic.update({num: i})
        return [dic.get(num, -1) for num in nums]


if __name__ == '__main__':
    solution = Solution().smallerNumbersThanCurrent(nums=[8, 1, 2, 2, 3])
    print(solution)
