#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-23 20:51
FileName: P0645. 错误的集合
Description:
"""
from typing import List
from collections import defaultdict


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        repeat, missing = 0, 0
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1
        for i in range(1, len(nums) + 1):
            if dic[i] == 2:
                repeat = i
            if dic[i] == 0:
                missing = i
        return [repeat, missing]


if __name__ == '__main__':
    solution = Solution().findErrorNums([1, 2, 2, 4])
    print(solution)
