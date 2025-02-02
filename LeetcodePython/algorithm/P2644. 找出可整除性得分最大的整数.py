#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-02 13:11
FileName: P2644. 找出可整除性得分最大的整数
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        dic = {divisor: sum(num % divisor == 0 for num in nums) for divisor in divisors}
        maximum = max(dic.values())
        return min([num for num, cnt in dic.items() if cnt == maximum])


if __name__ == '__main__':
    solution = Solution().maxDivScore(nums=[2, 9, 15, 50], divisors=[5, 3, 7, 2])
    ic(solution)
