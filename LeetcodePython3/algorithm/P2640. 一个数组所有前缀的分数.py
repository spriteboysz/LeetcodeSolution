#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-03 09:38
FileName: 面试题/P2640. 一个数组所有前缀的分数.py
Description: 
"""
from typing import List


class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        maximum = nums[0]
        acc = 0
        scores = []
        for num in nums:
            maximum = max(maximum, num)
            acc += num + maximum
            scores.append(acc)
        return scores


if __name__ == '__main__':
    solution = Solution().findPrefixScore([2, 3, 7, 5, 10])
    print(solution)
