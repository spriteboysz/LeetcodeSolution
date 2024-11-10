#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-10 09:07
FileName: P0001. 两数之和
Description:
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {num: i for i, num in enumerate(nums)}
        for i, num in enumerate(nums):
            another = target - num
            if another in index and i != index.get(another):
                return [i, index.get(another)]
        return []


if __name__ == '__main__':
    s = Solution().twoSum(nums=[2, 7, 11, 15], target=9)
    print(s)
