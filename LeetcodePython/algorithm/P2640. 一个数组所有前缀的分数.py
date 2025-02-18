#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-18 22:56
FileName: P2640. 一个数组所有前缀的分数
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        maximum, convert = nums[0], []
        for num in nums:
            maximum = max(maximum, num)
            convert.append(num + maximum)
        score, acc = [], 0
        for num in convert:
            acc += num
            score.append(acc)
        return score


if __name__ == '__main__':
    solution = Solution().findPrefixScore(nums=[2, 3, 7, 5, 10])
    ic(solution)
