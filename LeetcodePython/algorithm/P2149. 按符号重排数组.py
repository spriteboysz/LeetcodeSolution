#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-10 23:06
FileName: P2149. 按符号重排数组
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = [num for num in nums if num > 0]
        negative = [num for num in nums if num < 0]
        nums[::2], nums[1::2] = positive, negative
        return nums


if __name__ == '__main__':
    solution = Solution().rearrangeArray(nums=[3, 1, -2, -5, 2, -4])
    ic(solution)
