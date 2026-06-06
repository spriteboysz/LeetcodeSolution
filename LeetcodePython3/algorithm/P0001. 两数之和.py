#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-06 12:26
FileName: P0001. 两数之和.py
Description:
"""
from typing import List
from collections import defaultdict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = defaultdict(list)
        for i, num in enumerate(nums):
            dic[num].append(i)
        for i, num in enumerate(nums):
            if (indexes := dic.get(target - num, [])) and i != indexes[-1]:
                return [i, indexes[-1]]
        return []


if __name__ == '__main__':
    solution = Solution().twoSum(nums=[2, 7, 11, 15], target=9)
    print(solution)
