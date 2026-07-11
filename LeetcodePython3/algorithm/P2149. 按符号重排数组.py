#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-10 23:09
FileName: P2149. 按符号重排数组.py
Description:
"""
from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive, negative = [], []
        for num in nums:
            if num > 0:
                positive.append(num)
            else:
                negative.append(num)
        nums[::2], nums[1::2] = positive, negative
        return nums


if __name__ == '__main__':
    solution = Solution().rearrangeArray(nums=[3, 1, -2, -5, 2, -4])
    print(solution)
