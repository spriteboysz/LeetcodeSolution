#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-11 11:04
FileName: P0238. 除了自身以外数组的乘积.py
Description:
"""
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if set(nums) == {0} or nums.count(0) >= 2:
            return [0] * len(nums)
        product = 1
        for num in nums:
            if num == 0:
                continue
            product *= num
        ans, flag = [], nums.count(0) > 0
        for num in nums:
            if num == 0:
                ans.append(product)
            else:
                ans.append(0 if flag else (product // num))
        return ans


if __name__ == '__main__':
    solution = Solution().productExceptSelf(nums=[-1, 1, 0, -3, 3])
    print(solution)
