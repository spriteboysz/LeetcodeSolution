#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-17 23:18
FileName: P0238. 除自身以外数组的乘积
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cnt = sum(num == 0 for num in nums)
        if cnt >= 2:
            return [0] * len(nums)
        product = 1
        for num in filter(lambda num: num != 0, nums):
            product *= num
        if cnt == 1:
            ans = [0] * len(nums)
            for i, num in enumerate(nums):
                if num == 0:
                    ans[i] = product
            return ans
        return [product // num for num in nums]


if __name__ == '__main__':
    solution = Solution().productExceptSelf(nums=[1, 2, 3, 4])
    ic(solution)
